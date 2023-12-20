import pandas as pd
import telebot
import numpy as np
import os
from telebot import types
import openpyxl 
# ================================
flage_start=True
chat_id_user=[]
error=""
API_ID  = 27092043
API_HASH = "6e343973c3c214c81ba9dda53ffa5432"
TOKEN= "6516334569:AAGFh6qe80neQfNZ--JbgukqNn0TxICBaNw"
bot_token_1='6366799905:AAFmyfn66XPDKhZBswa6zr_cX7JhU4xWp1E'



TOKEN = "6024627311:AAERQ_NH4bupM1DGNUyE194zk2DtoBHGi7Q"
bot = telebot.TeleBot(TOKEN)
# df = pd.read_excel('text.xlsx')
# user=df.shape[0]






# if user!=0:
# #---------------Upload_user_history_from_file----------

#     df2 = pd.read_excel('example.xlsx', sheet_name="Sheet1")
#     chat_id_use = df2.iloc[:, 0].values

 
# else:
#       error="مشخصات کاربری وجود  ندارد ."






@bot.message_handler(commands=['startBot'])
def send_welcome(message):
         bot.reply_to(message,"ربات فعال شد.")


@bot.message_handler(func=lambda message: True, content_types=['photo'], commands=['get'])
def some_function(message):
    # Get the chat ID of the user who sent the photo
    user_chat_id = message.chat.id

    # Your array of other chat IDs (replace with your actual data)
    other_chat_ids = [12345678, 98765432, ...]

    # Iterate through other chat IDs and send the same message
    for chat_id in other_chat_ids:
        # Use the Telegram bot API to send the message
        bot.send_message(chat_id, f"User {user_chat_id} sent a photo: {message.caption}")

    # You can also handle the image part here if needed
    # ...

    # Reply to the user (optional)
    bot.reply_to(message, "Message forwarded to other users!")
bot.infinity_polling(timeout=40)
# @bot.message_handler(commands=['send'])
# def get_message(message):
#     bot.reply_to(message,"پیام مورد نطر را وارد کنید ."+"درصورتی که مایل به ادامه این  عملیات نیستید. کلمه cansel را وارد کنید.")
#     bot.register_next_step_handler(message, sender_Message)






# def sender_Message(message):
#   global chat_id_user
#   if message.text=="cansel":
#          bot.reply_to(message,"عملیات لغو شد")
#   else:     

#         temp_message=str(message.text)


#         for i in len(chat_id_user):
#             bot.send_message(i,temp_message) 
          
#         bot.reply_to(message,"پیام مورد نظر برای همه کاربران ارسال شد ")


# @bot.message_handler(func=lambda message: True, content_types=['photo'],commands=['get'])
# def some_function(message):
#     print(message.caption) # This will be your caption.
#     bot.reply_to(message,image)
 