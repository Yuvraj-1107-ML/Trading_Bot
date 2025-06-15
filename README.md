# 📈 Python Binance Testnet Trading Bot Using Python

This project is a beginner-friendly, educational **cryptocurrency trading bot** built in Python.
It connects to the **Binance Futures Testnet**, allowing you to test trading strategies with zero risk using virtual funds.

---

## 🚀 Features

✅ Connects securely to Binance Futures **Testnet**
✅ Place **market**, **limit**, **OCO**, or **stop** orders
✅ Cancel open orders anytime
✅ View account balance, open positions & trade history
✅ Clean, modular Python code
✅ Optional **Flask web interface** for easy interaction
✅ Detailed logs of API requests & responses

---

## 📂 Project Structure

```
.
├── bot.py          # Core trading bot logic
├── app.py          # Flask web server 
├── screenshot.png  
├── requirements.txt
└── README.md
```

---

## 🧰 Requirements

* Python 3.8+
* Binance Futures Testnet account
* Binance Testnet API key & secret
* Python packages:

  ```
  python-binance
  Flask (optional)
  ```

---

## ⚙️ Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Yuvraj-1107-ML/Trading_Bot.git
cd Trading_Bot
```

---

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Get Your Binance Testnet API Credentials

* Register on [Binance Futures Testnet](https://testnet.binancefuture.com)
* Create an API key and secret
* Enable Futures for your testnet account

---

### 5️⃣ DEMO API Keys

```python
API_KEY = 'RzrXosz2iAbphTwe75TfaQ7HQfLDXSEjlan7SVKUlgiN244DY1AZ5pdrHLhaqdmI'
API_SECRET = 'oH63K86VjVIL2CqTrWlyNi4WOiEr1ckmBpxIo3bFAZwf58WYGZzuHPH8xodyV8Qk'

```

---


**Run the core bot script:**

```bash
python bot.py
```

or

**Run the Flask web server:**

```bash
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🖼️ Demo User Interface

Below is an example of the web interface for placing orders and viewing bot status:

![Demo Screenshot](screenshot.png)

> **Tip:** Replace `screenshot.png` with your own UI screenshot!

---


## ⚠️ Disclaimer

* This bot **only uses the Binance Testnet** — no real money involved.
* **Do NOT use with real funds.**

---


---

## ✉️ Contact

Feel free to reach out for feedback, looking forward to your response


---

## ✅ Next Steps

* 📌 Replace `YOUR_TESTNET_API_KEY` and `YOUR_TESTNET_API_SECRET` in `config.py`.
* 📸 Add your own screenshot named `screenshot.png`.
* 🏁 Test and modify the bot logic to fit your strategy!
