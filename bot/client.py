from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://testnet.binancefuture.com"

def get_client():
    client = Client(
        api_key=os.getenv("API_KEY"),
        api_secret=os.getenv("API_SECRET")
    )

    # CRITICAL: switch to futures testnet
    client.FUTURES_URL = BASE_URL

    return client