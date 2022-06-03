
import os
import telebot
from functions import *
from  appmain import create_reply
API_KEY = os.environ['bot_API_KEY']
bot = telebot.TeleBot(API_KEY)

def check_link(message):
  return message.text.startswith('https://twitter.com')

@bot.message_handler(func=check_link)
def greet(message):
  bot.reply_to(message,create_reply(str(message.text)))
  file = open('data.csv','rb')
  bot.send_document(message.chat.id,  file)

# print(type(API_KEY))
# print(create_reply('https://twitter.com/Zionbonzo/status/1529590373672275971?t=FhW_2agTq7a71DXF9_G1Eg&s=19')) 

bot.polling()