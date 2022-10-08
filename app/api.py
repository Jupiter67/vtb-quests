"""
API сервиса квестов
"""

from fastapi import APIRouter
from fastapi.exceptions import HTTPException

router = APIRouter(prefix='/api')


@router.get('/foo')
def bar():
    return 'bar'
