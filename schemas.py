from pydantic import BaseModel



class QuoteBase(BaseModel):
    text: str
    author: str | None = None


class QuoteCreate(QuoteBase):
    pass


class Quote(QuoteBase):
    id: int

    class Config:
        orm_mode = True
