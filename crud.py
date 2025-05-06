from sqlalchemy.orm import Session
from random import choice
import models, schemas

def get_all_quotes(db: Session):
    return db.query(models.Quote).all()


def create_quote(db: Session, quote: schemas.QuoteCreate):
    db_quote = models.Quote(**quote.dict())
    db.add(db_quote)
    db.commit()
    db.refresh(db_quote)
    return db_quote



def get_random_quote(db: Session):
    quotes = get_all_quotes(db)
    return choice(quotes) if quotes else None


def delete_quote(db: Session, quote_id: int):
    quote = db.query(models.Quote).filter(models.Quote.id == quote_id).first()
    if quote:
        db.delete(quote)
        db.commit()
    return quote

