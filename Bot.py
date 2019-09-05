import telebot

bot= telebot.TeleBot('')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Send me a sticker to get his ID')
@bot.message_handler(content_types=['sticker'])
def send_message(message):
    a= str(message)
    b= a[a.index('file_id'):]
    id= b[:b.index(',')]
    result= id.replace("'", '')
    result2 = result.replace('file_id', '')
    text= str('This is the ID of your sticker ')
    bot.send_message(message.chat.id,text + result2)
bot.polling()