import telebot
import os
from loguru import logger
from utils.jsonio import write_json
from utils.keyboard import keyboards
#import emoji
#from math import *

class Bot:
	def __init__(self):
		self.bot = telebot.TeleBot(os.environ['TELEGRAM_BOT'])
		self.echo_all = self.bot.message_handler(
			func = lambda message: True
		)(self.echo_all)

	def run(self):
		logger.info('Bot is running...')
		self.bot.infinity_polling()

	def echo_all(self, message):
		write_json(message.json, 'message.json')
		#self.bot.reply_to(message, eval(message.text))
		self.bot.send_message(message.chat.id, message.text, reply_markup=keyboards.main)


if __name__ == '__main__':
	logger.info('Bot started')
	bot = Bot()
	bot.run()
