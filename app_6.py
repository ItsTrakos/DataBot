#حقوقي شرفك تلعب بيها تلعب بشرفك
import requests
import telebot
import random
from telebot import types
from time import sleep




token = input('[~] Enter Token : ')
bot = telebot.TeleBot(token)
#trakos
@bot.message_handler(commands=['start'])
def send_welcome(message):
	first = message.chat.first_name
	bot.send_message(message.chat.id,f"*Hi ,  send Instagram User id To check date Account Create \nBy @ttrakos | @trprogram*")
@bot.message_handler(func=lambda m: True)
def Get(message):
		msg = message.text
		bot.send_message(message.chat.id, text="تم الاختيار بنجاح الرجاء الانتظار ..")
		re = requests.get(f"https://o7aa.pythonanywhere.com/?id={msg}")   
		ree = re.json()
		r = ree['id']
		rt = ree['data']
		bot.send_message(message.chat.id, text=f"*id : {r}\nDate Create : {rt}\nBy | @ttrakos | @trprogram الرجاء الاشتراك ❤️*",parse_mode="markdown")

bot.polling(True)
