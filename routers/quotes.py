from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import schemas, crud

router = APIRouter(
    prefix="/quotes",
    tags=["Quotes"]
)

@router.get("/", response_model=list[schemas.Quote])
def read_quotes(db: Session = Depends(get_db)):
    return crud.get_all_quotes(db)



@router.post("/", response_model=schemas.Quote)
def add_quote(quote: schemas.QuoteCreate, db: Session = Depends(get_db)):
    return crud.create_quote(db, quote)


@router.get("/random", response_model=schemas.Quote)
def random_quote(db: Session = Depends(get_db)):
    quote = crud.get_random_quote(db)
    if not quote:
        raise HTTPException(status_code=404, detail="No quotes found")
    return quote


@router.delete("/{quote_id}", response_model=schemas.Quote)
def delete_quote(quote_id: int, db: Session = Depends(get_db)):
    quote = crud.delete_quote(db, quote_id)
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")
    return quote






