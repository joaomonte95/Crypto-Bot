# Crypto-Bot

## Function:
This bot intends to show important data about crypto currencies, capted by web scrapping in the site https://coinmarketcap.com/.

## Running the bot
To run the bot, you must add a token.json as {"TOKEN":"<TOKEN NUMBER>"} in root directory
and run "python bot.py" in your terminal.
  
## Requirements:

* python-telegram-bot: pip install python-telegram-bot --upgrade

* requests: pip install requests

* beautifulsoup: pip install beautifulsoup4

* mongoDB

## Functions:

* /start: Show start message

* /help: Show all commands

* /data cryptoCurrency  - show the most import data about the argument crypto currency
