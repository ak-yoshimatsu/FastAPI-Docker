from fastapi import FastAPI, status
from api.routers import auth

app = FastAPI()


@app.get('/', tags=['home'], status_code=status.HTTP_204_NO_CONTENT)
def index():
    return {'data': 'Hello!!!'}


app.include_router(auth.router)
