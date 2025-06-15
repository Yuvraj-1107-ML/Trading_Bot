# bot.py
from binance.client import Client
from binance.exceptions import BinanceAPIException
import logging

logger = logging.getLogger(__name__)

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)
        if testnet:
            self.client.API_URL = 'https://testnet.binance.vision/api'

    def get_current_price(self, symbol):
        try:
            ticker = self.client.get_symbol_ticker(symbol=symbol)
            return float(ticker['price'])
        except BinanceAPIException as e:
            logger.error(f"Error fetching price: {e}")
            return None

    def place_order(self, symbol, side, order_type, quantity, price=None, stop_price=None, stop_limit_price=None):
        try:
            if order_type == 'MARKET':
                if side == 'BUY':
                    order = self.client.order_market_buy(symbol=symbol, quantity=quantity)
                else:
                    order = self.client.order_market_sell(symbol=symbol, quantity=quantity)
            elif order_type == 'LIMIT':
                if not price:
                    raise ValueError("Price must be provided for LIMIT orders.")
                if side == 'BUY':
                    order = self.client.order_limit_buy(
                        symbol=symbol,
                        quantity=quantity,
                        price=str(price),
                        timeInForce='GTC'
                    )
                else:
                    order = self.client.order_limit_sell(
                        symbol=symbol,
                        quantity=quantity,
                        price=str(price),
                        timeInForce='GTC'
                    )
            elif order_type == 'OCO':
                if side != 'SELL':
                    raise ValueError("Binance only supports OCO SELL orders.")
                if not (price and stop_price and stop_limit_price):
                    raise ValueError("Price, Stop Price, and Stop Limit Price must be provided for OCO orders.")
                order = self.client.create_oco_order(
                    symbol=symbol,
                    side=side,
                    quantity=quantity,
                    price=str(price),
                    stopPrice=str(stop_price),
                    stopLimitPrice=str(stop_limit_price),
                    stopLimitTimeInForce='GTC',
                    priceProtect=True
                )
            else:
                raise ValueError("Invalid order type.")
            logger.info(f"{side} {order_type} order executed: {order}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            return {'error': str(e)}
        except Exception as e:
            logger.error(f"Unexpected Error: {e}")
            return {'error': str(e)}

    def get_balance(self, asset):
        try:
            account_info = self.client.get_account()
            for balance in account_info['balances']:
                if balance['asset'] == asset:
                    return {
                        'asset': asset,
                        'free': balance['free'],
                        'locked': balance['locked']
                    }
            return {'asset': asset, 'free': '0', 'locked': '0'}
        except BinanceAPIException as e:
            logger.error(f"Error fetching balance: {e}")
            return None
