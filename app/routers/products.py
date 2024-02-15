from fastapi import APIRouter
from ..utils.db import get_products

router = APIRouter(prefix='/products', tags=['Products'])


@router.get('/get-products')
async def get_all_products():
    try:
        db_products = get_products()

        products_cursor = await db_products.find({}).to_list(length=None)

        products = [{**product, "_id": str(product["_id"])}
                    for product in products_cursor]

        return {"data": products, "count": len(products)}
    except Exception as e:
        return {"error": f"{e}"}
