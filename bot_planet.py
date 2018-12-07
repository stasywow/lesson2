import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import datetime

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
         'urllib3_proxy_kwargs': {'username': 'learn',
                                  'password': 'python'}
         }

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

log = logging.getLogger(__name__)


def greet_user(bot, update):
    text = 'Привет!'
    log.info(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text
    log.info(user_text)
    update.message.reply_text("Кококо")


def nice(bot, update):
    text = 'Кококо'
    log.info(text)
    update.message.reply_text(text)


def planet(bot, update, args):
    log.info(args)
    plan = ''.join(args)
    plan = plan.capitalize()
    log.info(plan)
    date = datetime.datetime.now()

    right_date = date.strftime('%Y/%m/%d')
    log.info(right_date)
    plan_time = getattr(ephem, plan)(right_date)
    log.info(plan_time)
    text_const = ephem.constellation(plan_time)
    log.info(text_const)
    update.message.reply_text(text_const)


def unknown(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")


def main():
    mybot = Updater(os.getenv('API_KEY'), request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("hello", nice))
    dp.add_handler(CommandHandler("planet", planet, pass_args=True))
    dp.add_handler(MessageHandler(Filters.command, unknown))
    
    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
