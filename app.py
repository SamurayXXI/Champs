from fastapi import FastAPI

from routers import championships

app = FastAPI()
app.include_router(championships.router, prefix="/championships")
