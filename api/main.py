from fastapi import FastAPI

from .s1.routes import medical_staff
from .s2.routes import patients

app = FastAPI()


@app.get("/", tags=["main"])
def index():
    return {"data": "Hello!!!"}


app.include_router(medical_staff.router)
app.include_router(patients.router)
