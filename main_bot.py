
            
import telebot
import pandas as pd
import openpyxl
from config import API_ID,API_HASH,TOKEN
import time

# Initialize the Telegram bot
bot_api = API_ID
bot_api_hash = API_HASH
bot_token = TOKEN
flag_active=False #for activate bot 

user_chat_id=[]
bot = telebot.TeleBot(bot_token)
df = pd.read_excel('text.xlsx')

# =====================================

df = pd.read_excel('user.xlsx', sheet_name="Sheet1")
user_chat_id = df.iloc[:, 0].values

# =======================================

#start bot for send news 
@bot.message_handler(commands=['start'])
def handle_start(message):
    
    global flag_active ,user_chat_id
    chat_id=message.chat.id
    if  chat_id not in user_chat_id:
         
        user_chat_id.append(message.chat.id)
         
        with open("user.xlsx", 'rb') as file:
           temp = pd.read_excel('user.xlsx', sheet_name="Sheet1")
           temp.drop(index=range(0, len(temp)), inplace=True)
           temp.to_excel('user.xlsx', index=False)
        df2 = pd.DataFrame({'chat_id': user_chat_id}) 
        df2.to_excel('user.xlsx', index=False)
        bot.reply_to(message,'✅'+' ربات اطلاع رسانی  نسرا برای  شما فعال گردید ') 

    else:
         bot.reply_to(message,'✅'+' ربات اطلاع رسانی  نسرا  هم اکنون برای  شما فعال است. ') 
     


#======================active=bot==========================================   
@bot.message_handler(commands=['active'])
def handle_start(message):
    
    global flag_active 
    if flag_active==True:
        bot.reply_to(message,"❌"+'ربات در حال حاضر فعال می باشد.')
    else:
        
        flag_active=True   
        bot.reply_to(message,'✅ربات فعال شد.')   

    

@bot.message_handler(commands=['send'])
    
def some_function(message):
    if flag_active==True:   
      bot.reply_to(message,"پیام مورد نظر را وارد کنید.")
      bot.register_next_step_handler(message,some_function)
    else:
        bot.reply_to(message, "❎"+"ربات در حال حاضر غیر فعال است.")

    
def some_function(message):
      global flag_active,user_chat_id
   
               
      if message.photo:
        photo = message.photo[-1]
        file_id = photo.file_id
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        for user_id in user_chat_id:
             bot.send_photo(user_chat_id , downloaded_file, caption=message.caption)
       
        bot.reply_to(message, "✅"+"پیام مورد نظر شما برای تمام  کاربران و گروه ها ارسال شد.")
      elif message.text:
           bot.send_photo(-4020519220 , message.text)
           bot.reply_to(message, "✅"+"پیام مورد نظر شما برای تمام  کاربران و گروه ها ارسال شد.")
      else:
        bot.reply_to(message, "❎"+"فرمت پیام مورد نظر شما صحیح نمی باشد.")


@bot.message_handler(commands=['add'])  
def some_function(message):
     
     if flag_active==True:   
      bot.reply_to(message,"شناسه مورد نطز را وارد کنید .")
      bot.register_next_step_handler(message,save_chat_id)
     else:
              bot.reply_to(message, "❎"+"فرمت پیام مورد نظر شما صحیح نمی باشد.")
def save_chat_id(message):
      
      global flag_active,user_chat_id
      new_chat_id=int(message.text)

      if  new_chat_id not in user_chat_id:
         
        
         user_chat_id.append(message.chat.id)

         with open("user.xlsx", 'rb') as file:
            temp = pd.read_excel('user.xlsx', sheet_name="Sheet1")
            temp.drop(index=range(0, len(temp)), inplace=True)
            temp.to_excel('user.xlsx', index=False)

         df2 = pd.DataFrame({'chat_id': user_chat_id}) 
         df2.to_excel('user.xlsx', index=False)
         bot.reply_to(message,'✅'+'شناسه کاربر افزوده شد.') 




      else:
         bot.reply_to(message,'✅'+'شناسه کاربر مورد نظر در حال حاطر موجود است') 

   
               
      
 
     
     
  

@bot.message_handler(commands=['deactive'])
def handle_end(message):
    global flag_active
    if flag_active==True:
        flag_active=False
        bot.reply_to(message,"✅"+'ربات غیر فعال شد')
    else:
        
        bot.reply_to(message,"❌"+"ربات درحال حاضر غیر فعال می باشد.")    
bot.infinity_polling(timeout=40)
        



  