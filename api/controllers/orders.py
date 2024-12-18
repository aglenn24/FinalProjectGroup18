from sqlalchemy.orm import Session, relationship
from fastapi import HTTPException, status, Response, Depends
from ..models import orders as model
from sqlalchemy.exc import SQLAlchemyError
from ..models.promo_codes import PromoCodes
from ..controllers.resources import check_resources, subtract_resources
from datetime import datetime


def create(db: Session, request):
    new_item = model.Order(
        # placeholders
        # customer
        customer_name=request.customer_name,
        customer_address=request.customer_address,
        customer_email=request.customer_email,
        customer_phone=request.customer_phone,
        description=request.description,
        
        # tracking/order info
        # might need to generate tracking number outside of thing
        tracking_number=request.tracking_number,
        order_status=request.order_status,
        order_date=request.order_date,
        total_price=request.calculate_total_price(),
        
        # might need to generate one somewhere
        review_text = request.review_text,
        score = request.score,
        
        card_info=request.card_info,
        transaction_status=request.transaction_status,
        payment_type=request.payment_type
    )

    try:
        check_resources(db, new_item, request.amount)
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)

    return new_item


def read_all(db: Session):
    try:
        result = db.query(model.Order).all()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return result


def read_one(db: Session, item_id):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item


def update(db: Session, item_id, request):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        update_data = request.dict(exclude_unset=True)
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()

def update_review(db: Session, item_id, request):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found!")
        update_data = {
            "review_text": request.review_text if request.review_text else "",
            "score": request.score if request.score else 3
        }
        item.update(update_data, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return item.first()

def update_order_status(db: Session, tracking_number: str, new_status: str):
    try:
        order = db.query(model.Order).filter(model.Order.tracking_number == tracking_number)
        if not order.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found!")
        order.update({"order_status": new_status}, synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return order.first()


def delete(db: Session, item_id):
    try:
        item = db.query(model.Order).filter(model.Order.id == item_id)
        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id not found!")
        item.delete(synchronize_session=False)
        db.commit()
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def calculate_total_price(self):
    base_price = self.total_price * self.amount
    if check_promo_code(self.db, self.promo_code):
        discount_percent = self.promo_code.discount_percent
        discount_price = base_price * discount_percent / 100
        self.total_price = base_price - discount_price
    else:
        self.total_price = base_price

def check_promo_code(db: Session, promo_code):
    promo = db.query(PromoCodes).filter_by(code=promo_code).first()
    if promo is None or is_promo_code_expired(db, promo_code):
        return False
    return True


def is_promo_code_expired(db: Session, promo_code):
    promo = db.query(PromoCodes).filter_by(code=promo_code).first()
    if promo is None:
        return True
    return promo.expiration < datetime.now()

def search_by_tracking_number(db: Session, tracking_number):
    try:
        order = db.query(model.Order).filter(model.Order.tracking_number == tracking_number).first()
        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tracking number not found!")
    except SQLAlchemyError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e.__dict__['orig']))
    return order
