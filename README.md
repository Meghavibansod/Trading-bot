## 📈 Binance Futures Testnet Trading Bot (Python)

A simplified Python-based trading bot that interacts with Binance USDT-M Futures Testnet to place Market and Limit orders via a CLI interface.

The project demonstrates API integration, structured code design, logging, and error handling.


🚀 Features


✅ Place Market Orders

✅ Place Limit Orders

✅ Supports BUY / SELL

✅ Command-line interface (CLI) using argparse

✅ Input validation for trading parameters

✅ Structured architecture (API layer + CLI layer)

✅ Logging of:

API requests

API responses


Errors and exceptions

✅ Error handling for:

Invalid inputs
API failures
Network issues



🏗️ Project Structure

trading_bot/
│
├── bot/
│   ├── client.py          # Binance API client wrapper
│   ├── orders.py          # Order placement logic
│   ├── validators.py      # Input validation logic
│   ├── logging_config.py  # Logging setup
│
├── cli.py                 # CLI entry point
├── bot.log                # Log file (generated after run)
├── requirements.txt
├── README.md
└── .gitignore



⚙️ Setup Instructions

1️⃣ Clone the repository

git clone https://github.com/YOUR_USERNAME/trading-bot.git
cd trading-bot

2️⃣ Create virtual environment 

python -m venv venv

Activate:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Set environment variables

Create a .env file:

API_KEY=your_testnet_api_key

API_SECRET=your_testnet_api_secret




▶️ How to Run

📌 Place MARKET Order

python cli.py --symbol BTCUSDT --side BUY --order_type MARKET --quantity 0.001

📌 Place LIMIT Order

python cli.py --symbol BTCUSDT --side SELL --order_type LIMIT --quantity 0.001 --price 60000



📤 Output Example

========== ORDER REQUEST ==========

Symbol     : BTCUSDT
Side       : BUY
Type       : MARKET
Quantity   : 0.001

Placing order...

========== ORDER RESPONSE ==========

Order ID   : 123456789
Status     : FILLED
Executed   : 0.001
Avg Price  : 42150.5


✅ Order placed successfully



🧾 Logging

All API activity is stored in:

bot.log

Includes:

Request payloads

API responses



📊 Assumptions

Only Binance Futures Testnet (USDT-M) is used

Market and Limit orders only

No live trading support (test environment only)

API keys are stored securely in .env


🧪 Example Test Cases

✔ MARKET BUY

Symbol: BTCUSDT

Quantity: 0.001



✔ LIMIT SELL

Symbol: BTCUSDT

Price: 60000

Quantity: 0.001




⚠️ Security Notes

Never expose API keys in code

.env file is excluded using .gitignore

Logs do not contain sensitive credentials




📦 requirements.txt

python-binance

python-dotenv



👨‍💻 Author

Built as part of a Python Developer assessment task for Binance Futures Testnet trading automation.



🟢 Status

✔ Market Order Working
✔ Limit Order Working
✔ CLI Functional
✔ Logging Enabled
