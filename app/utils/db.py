import os
from motor import motor_asyncio
from dotenv import load_dotenv

load_dotenv()


def get_products():
    client = motor_asyncio.AsyncIOMotorClient(os.environ["DIP_MONGO_URI"])["main"]

    return client["products"]
