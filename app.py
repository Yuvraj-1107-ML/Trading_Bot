# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from bot import BasicBot
from binance.client import Client as PublicClient
import logging
import os

if not os.path.exists('logs'):
    os.makedirs('logs')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("logs/trading_bot.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = "supersecretkey"

@app.route('/', methods=['GET', 'POST'])
def index():
    balance_asset = None
    balance_usdt = None
    order_result = None

    if request.method == 'POST':
        api_key = request.form['api_key']
        api_secret = request.form['api_secret']
        symbol = request.form['symbol'].upper()
        order_type = request.form['order_type'].upper()
        side = request.form['side'].upper()
        quantity = float(request.form['quantity'])

        limit_price = request.form.get('price')
        stop_price = request.form.get('stop_price')
        stop_limit_price = request.form.get('stop_limit_price')

        bot = BasicBot(api_key, api_secret, testnet=True)

        # Validate required prices
        if order_type == 'LIMIT' and not limit_price:
            flash("Price is required for LIMIT orders.", "danger")
            return redirect(url_for('index'))
        if order_type == 'OCO' and not (limit_price and stop_price and stop_limit_price):
            flash("Price, Stop Price, and Stop Limit Price are required for OCO orders.", "danger")
            return redirect(url_for('index'))

        result = bot.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=float(limit_price) if limit_price else None,
            stop_price=float(stop_price) if stop_price else None,
            stop_limit_price=float(stop_limit_price) if stop_limit_price else None
        )

        if result and 'error' not in result:
            flash(f"{side.capitalize()} {order_type.capitalize()} order placed successfully!", "success")
        else:
            flash(f"Order failed: {result.get('error', 'Unknown error')}", "danger")

        base_asset = symbol.replace('USDT', '')
        balance_asset = bot.get_balance(base_asset)
        balance_usdt = bot.get_balance('USDT')
        order_result = result

    return render_template('index.html',
                           balance_asset=balance_asset,
                           balance_usdt=balance_usdt,
                           order_result=order_result)


@app.route('/price')
def price():
    symbol = request.args.get('symbol', 'BTCUSDT').upper()
    public_client = PublicClient()
    ticker = public_client.get_symbol_ticker(symbol=symbol)
    return jsonify({'price': float(ticker['price'])})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # use 5000 locally, or the platform's port
    app.run(host="0.0.0.0", port=port)

    app.run(debug=False)
