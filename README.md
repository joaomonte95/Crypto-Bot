# Crypto-Bot

## Function:
This bot intends to show important data about crypto currencies, obteined in https://coinmarketcap.com/ 's API.

## Running the bot
add a your dev key to mongodb admin bank, token collection.
{_id:...,"name":"token","token":<your token>}
  
Run bot.py
## Requirements:

* python-telegram-bot: pip install python-telegram-bot --upgrade

* requests: pip install requests

* beautifulsoup: pip install beautifulsoup4

* mongoDB

## Functions:

* /start: Show start message

* /help: Show all commands

* /data cryptoCurrency  - show the most import data about the argument crypto currency
