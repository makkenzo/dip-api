from .routers import products, auth, user

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI


app = FastAPI(title="Do It PCelf API")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(products.router)
app.include_router(auth.router)
app.include_router(user.router)
