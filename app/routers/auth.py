from fastapi import APIRouter, Request, status, Response

from ..models.auth import RegistrationModel
from svix.webhooks import Webhook, WebhookVerificationError

from ..utils.db import get_users_db


router = APIRouter(prefix="/auth", tags=["Authorization"])


@router.post("/wh/sign-up", status_code=status.HTTP_204_NO_CONTENT)
async def webhook_handler(req: Request, response: Response):
    wh_secret = "whsec_Hxa5+Yn0xsu6jmM50VbJPygrSsijwWNK"

    headers = req.headers
    payload = await req.body()

    db_users = get_users_db()

    try:
        wh = Webhook(wh_secret)
        msg = wh.verify(payload, headers)

        data = {
            "email": msg["data"]["email_addresses"][0]["email_address"],
            "image_url": msg["data"]["image_url"],
            "first_name": msg["data"]["first_name"],
            "last_name": msg["data"]["last_name"],
        }

        user_in_db = await db_users.find_one({"email": data["email"]})

        if user_in_db is None:
            await db_users.insert_one(data)
    except WebhookVerificationError as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return
