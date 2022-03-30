from binance.client import Client

from dotenv import load_dotenv
import os
load_dotenv()


def get_current_price(token):
    client = Client(api_key=os.getenv("API_KEY"), api_secret=os.getenv("SECRET_KEY"))
    if token == 'DAI' or token == 'USDC' or token == 'USDT':
        return 1
    elif token == 'WMATIC' or token == 'WETH' or token == 'WBTC':
        try:
            new_token = token[1:]
            pair = new_token + 'BUSD'
            price = client.get_symbol_ticker(symbol=pair)
            return round(float(price['price']), 2)
        except:
            return 0
    else:
        try:
            pair = token + 'BUSD'
            price = client.get_symbol_ticker(symbol=pair)
            return round(float(price['price']), 2)
        except:
            return 0




