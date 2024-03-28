from fastapi import APIRouter, Request
from ..models.user import AddToCartModel

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/add-to-cart")
async def add_to_cart(req: Request, body: AddToCartModel):
    pass
