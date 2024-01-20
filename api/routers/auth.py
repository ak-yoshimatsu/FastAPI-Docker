from fastapi import APIRouter, status


router = APIRouter(tags=['auth'])


@router.post('/auth', status_code=status.HTTP_200_OK)
def login():
    return {'data': 'auth'}
