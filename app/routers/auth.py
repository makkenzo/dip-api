from fastapi import APIRouter, Request, status, Response

from ..models.auth import RegistrationModel
from svix.webhooks import Webhook, WebhookVerificationError


router = APIRouter(prefix="/auth", tags=["Authorization"])


@router.post("/wh/sign-up", status_code=status.HTTP_204_NO_CONTENT)
async def webhook_handler(req: Request, response: Response):
    wh_secret = "whsec_Hxa5+Yn0xsu6jmM50VbJPygrSsijwWNK"

    headers = req.headers
    payload = await req.body()

    try:
        wh = Webhook(wh_secret)
        msg = wh.verify(payload, headers)
        print(msg)
    except WebhookVerificationError as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return
