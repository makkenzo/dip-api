from fastapi import APIRouter, Request

from ..models.auth import RegistrationModel


router = APIRouter(prefix="/auth", tags=["Authorization"])

wh_secret = "whsec_Hxa5+Yn0xsu6jmM50VbJPygrSsijwWNK"


@router.post("/sign-up")
async def sign_up(req: Request, req_body: RegistrationModel):
    try:
        body = req_body.dict()
        print(body)
        return {"message": "ok"}
    except Exception as e:
        return {"error": f"{e}"}
