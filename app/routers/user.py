from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from ..models.user import AddToCartModel
from ..utils.db import get_users_db, get_products
from bson import ObjectId

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/add-to-cart")
async def add_to_cart(req: Request, body: AddToCartModel):
    try:
        users = get_users_db()

        user = await users.find_one({"uid": body.user_id})

        if user is not None:
            await users.update_one({"uid": body.user_id}, {"$addToSet": {"cart": body.item_id}})

            return JSONResponse(content={"message": "Item added to cart successfully"}, status_code=200)
        else:
            return JSONResponse(content={"message": "User not found"}, status_code=400)
    except Exception as e:
        return JSONResponse(content={"message": str(e)}, status_code=500)


@router.get("/get-cart/{uid}")
async def get_cart(req: Request, uid: str):
    try:
        users = get_users_db()
        products = get_products()

        user = await users.find_one({"uid": uid})

        if user is not None:
            cart_items = user.get("cart", [])
            cart_products = []

            for item_id in cart_items:
                product = await products.find_one({"_id": ObjectId(item_id)})
                if product:
                    # Преобразуем ObjectId в строку
                    product["_id"] = str(product["_id"])
                    cart_products.append(product)
                else:
                    return JSONResponse(
                        content={"message": f"Product with id {item_id} not found in the database"}, status_code=404
                    )

            return JSONResponse(content={"items": cart_products, "length": len(cart_products)}, status_code=200)
        else:
            return JSONResponse(content={"message": "User not found"}, status_code=400)
    except Exception as e:
        return JSONResponse(content={"message": str(e)}, status_code=500)


@router.delete("/remove-from-cart/{user_id}/{item_id}")
async def remove_from_cart(req: Request, user_id: str, item_id: str):
    try:
        users = get_users_db()

        user = await users.find_one({"uid": user_id})

        if user is not None:
            await users.update_one({"uid": user_id}, {"$pull": {"cart": item_id}})

            return JSONResponse(content={"message": "Item removed from cart successfully"}, status_code=200)
        else:
            return JSONResponse(content={"message": "User not found"}, status_code=400)
    except Exception as e:
        return JSONResponse(content={"message": str(e)}, status_code=500)
