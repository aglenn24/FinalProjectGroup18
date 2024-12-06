from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session
from ..controllers import sandwiches as controller  # Adjust the path as necessary
from ..schemas import sandwiches as schema  # Define appropriate schemas for OrderDetail
from ..dependencies.database import get_db  # Ensure get_db is correctly set up

router = APIRouter(
    tags=["Sandwiches"],
    prefix="/sandwiches"
)

@router.post("/", response_model=schema.Sandwich)
def create(request: schema.SandwichCreate, db: Session = Depends(get_db)):
    return controller.create(db=db, request=request)

@router.get("/", response_model=list[schema.Sandwich])
def read_all(db: Session = Depends(get_db)):
    return controller.read_all(db)

@router.get("/{item_id}", response_model=schema.Sandwich)
def read_one(item_id: int, db: Session = Depends(get_db)):
    return controller.read_one(db, item_id=item_id)

@router.put("/{item_id}", response_model=schema.Sandwich)
def update(item_id: int, request: schema.SandwichUpdate, db: Session = Depends(get_db)):
    return controller.update(db=db, request=request, item_id=item_id)

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(item_id: int, db: Session = Depends(get_db)):
    return controller.delete(db=db, item_id=item_id)
