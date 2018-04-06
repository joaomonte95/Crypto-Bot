from telegram.ext import JobQueue,Updater, CommandHandler, MessageHandler, Filters
from telegram import Bot
from Libs.db_querys import MongoQuerys
from Libs.scrapping import Scraping
import logging
import json

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

with open("token.json","r") as file_output:
    TOKEN = file_output.read()

TOKEN = json.loads(TOKEN)
TOKEN = TOKEN['TOKEN']

def start(bot,update):
    update.message.reply_text('Welcome to the crypto coin assitent bot! To get aknowledge about all my funcionalities, please type /help.')

def help(bot,update):
    update.message.reply_text("""
    Don't use <> symbols. They are present for visualization only!! \n
    Press "/data all" to see the top 100 crypto coins and their main data\n
    Press "/data <crypto coin name>" to inspect the whole data\n
    Press "/price <crypto coin name>" to inspect it's price\n
    Press "/rank <crypto coin name>" to inspect it's rank on https://coinmarketcap.com\n
    Press "/volume <crypto coin name>" to inspect the volume of transactions on past 24 hours \n
    Press "/change <crypto coin name>" to see how the value changed on past 24 hours\n
    """)

def echo(bot,update):
    pass

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def data(bot, update):
    coin_text = update.message.text.lower()
    args = coin_text.split(" ")[1::]
    args = " ".join(args)
    query = MongoQuerys()
    query_response = query.get_from_db({"name":f"{args}"})
    print(query_response)
    response = ""
    for k,v in query_response.items():
        if k!="_id":
            response += k + " : " + str(v) + " | "
    update.message.reply_text(response)

def db_update(bot,job):
    db = MongoQuerys()
    scrapper = Scraping()
    data = scrapper.main()
    db.drop_collections()
    for element in data:
        db.post_to_db(element)

def main():
    """Start the bot."""
    updater = Updater(TOKEN)
    job = updater.job_queue
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("data", data))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)
    job.run_repeating(db_update, interval=60, first=0)
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
