from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from telegram import ReplyKeyboardMarkup
import test
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import random
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token=test.token)

dispatcher = updater.dispatcher


def start (bot, update):
    while True:
        n = random.randint(6,7)
        ar = random.sample(population=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], k=n)
        arg = ''
        for i in ar:
            arg +=i
        try:
            req = Request('https://prnt.sc/%s' %(arg), headers={'User-Agent': 'Mozilla/5.0'})
            r = urlopen(req).read()
            soup = BeautifulSoup(r, "html.parser")
            table = soup.find('img', class_='no-click screenshot-image')
            if str(table).split('src="')[1][:-3] != '//st.prntscr.com/2018/10/13/2048/img/0_173a7b_211be8ff.png':
                for i in test.admin:
                    try: 
                        bot.send_message(i, str(table).split('src="')[1][:-3])
                    except:
                        pass
        except:
            pass


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling(timeout=5, clean=True )
