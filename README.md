<!DOCTYPE html>
<html>
<head>
    <title>Binance Futures Trading Bot</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6;">

<h1 align="center">🚀 Binance Futures Trading Bot</h1>

<p align="center">
<b>Python CLI Bot for Binance Futures Testnet (USDT-M)</b>
</p>

<hr>

<h2>📌 Overview</h2>
<p>
A lightweight Python application to place <b>Market</b> and <b>Limit</b> orders on Binance Futures Testnet.
Built with clean structure, validation, logging, and dual-mode usage (CLI + Interactive).
</p>

<h2>✨ Features</h2>
<ul>
<li>Place <b>MARKET</b> and <b>LIMIT</b> orders</li>
<li>Supports <b>BUY</b> and <b>SELL</b></li>
<li>CLI + Interactive modes</li>
<li>Input validation with clear messages</li>
<li>Logging of API requests, responses, and errors</li>
<li>Modular and clean code structure</li>
</ul>

<h2>🏗️ Project Structure</h2>
<pre>
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   ├── logging_config.py
│
├── cli.py
├── requirements.txt
├── README.txt
├── trading.log
</pre>

<h2>⚙️ Setup</h2>

<h3>1. Clone Repository</h3>
<pre>
git clone &lt;your-repo-link&gt;
cd trading_bot
</pre>

<h3>2. Install Dependencies</h3>
<pre>
pip install -r requirements.txt
</pre>

<h3>3. Configure API Keys</h3>
<p>Edit <b>cli.py</b> and add:</p>
<pre>
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
</pre>

<h2>▶️ Usage</h2>

<h3>CLI Mode</h3>
<pre>
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
</pre>

<h3>Limit Order Example</h3>
<pre>
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 100000
</pre>

<h3>Interactive Mode</h3>
<pre>
python cli.py
</pre>

<h2>📊 Sample Output</h2>
<pre>
ORDER REQUEST
Symbol   : BTCUSDT
Side     : BUY
Type     : MARKET
Quantity : 0.002

ORDER RESPONSE
Order ID     : 12345678
Status       : FILLED
Executed Qty : 0.002
Avg Price    : 64000

SUCCESS
</pre>

<h2>📝 Logging</h2>
<p>All logs are stored in:</p>
<pre>trading.log</pre>

<ul>
<li>API requests</li>
<li>API responses</li>
<li>Errors</li>
</ul>

<h2>⚠️ Error Handling</h2>
<ul>
<li>Invalid inputs</li>
<li>Missing parameters</li>
<li>API errors</li>
<li>Network failures</li>
</ul>

<h2>📌 Assumptions</h2>
<ul>
<li>Using Binance Futures Testnet (USDT-M)</li>
<li>Minimum order value ≥ 100 USDT</li>
<li>Valid API keys</li>
</ul>

<h2>📦 Requirements</h2>
<pre>
python-binance
</pre>

<h2>👨‍💻 Author</h2>
<p>Deepak Kumar Sahu</p>

<hr>

<p align="center">
<b>End of Document</b>
</p>

</body>
</html>
