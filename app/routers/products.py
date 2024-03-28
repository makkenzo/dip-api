from bson import ObjectId
from fastapi import APIRouter, Request
from ..utils.db import get_products
from fastapi import APIRouter, Query


router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/get-products")
async def get_all_products(page: int = Query(1, ge=1), limit: int = Query(4, ge=1, le=100), filter: str = Query(None)):
    try:
        db_products = get_products()

        if filter:
            products_cursor = await db_products.find({"name": {"$regex": filter, "$options": "i"}}).to_list(length=None)
        else:
            products_cursor = await db_products.find({}).to_list(length=None)

        start_index = (page - 1) * limit
        end_index = start_index + limit
        products_cursor = products_cursor[start_index:end_index]

        products = [{**product, "_id": str(product["_id"])} for product in products_cursor]

        return {"data": products, "count": len(products)}
    except Exception as e:
        return {"error": f"{e}"}


@router.get("/get-product/{product_id}")
async def get_product(product_id: str):
    try:
        db_products = get_products()
        product = await db_products.find_one({"_id": ObjectId(product_id)})

        if product:
            product["_id"] = str(product["_id"])
            return {"data": product}
        else:
            return {"error": "Product not found"}
    except Exception as e:
        return {"error": f"{e}"}
