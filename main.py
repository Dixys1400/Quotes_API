from fastapi import FastAPI
import models
from database import engine
from routers import quotes


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Inspiration Quotes API")


app.include_router(quotes.router)


