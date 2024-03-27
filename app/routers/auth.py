from bson import ObjectId
from fastapi import APIRouter
from ..utils.db import get_products
from fastapi import APIRouter, Query
from typing import List


router = APIRouter(prefix="/auth", tags=["Authorization"])


@router.post("/sign-up")
async def sign_up():
    try:
        return {"message": "ok"}
    except Exception as e:
        return {"error": f"{e}"}
