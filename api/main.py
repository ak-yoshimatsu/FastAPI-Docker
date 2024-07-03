from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class UserRequest(BaseModel):
    name: str = Field(max_length=10, examples=["山田太郎"])
    age: int = Field(examples=[29])


@app.get("/")
def index():
    return {"data": "Hello!!!"}


@app.post("/", response_model=UserRequest)
def store(request: UserRequest):
    return request


@app.get("/test")
def test():
    return {"data": "テストです！！"}
