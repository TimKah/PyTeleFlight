import telebot
import constants
import DBManager
import SQLManager
import FuncManager
import datetime
import KeyboardManager

bot = telebot.TeleBot(constants.token)

def log(message):
    print("{0} {1} (#{2}) said \"{3}\"".format(message.chat.first_name, message.chat.last_name, message.chat.id, message.text))
                #
            # # # # # 
        # # # # # # # # # 
    # # # # #       # # # # # 
# # # # # # # BEGIN # # # # # # # 
    # # # # #       # # # # # 
        # # # # # # # # # 
            # # # # #
                #
@bot.message_handler(commands=['start'])
def handle_text(message):
    log(message)
    SQLManager.findUser(message)
    FuncManager.showMenu(message)
# menu /events
@bot.message_handler(commands=['events'])
def handle_text(message):
    log(message)
    if SQLManager.getUserStrAttr(message, "status") == "menu":
        FuncManager.comEvents(message)
# events /?month
@bot.message_handler(commands=['1month'])
def handle_text(message):
    log(message)
    if SQLManager.getUserStrAttr(message, "status") == "events":
        FuncManager.showEvents(message, 1)
@bot.message_handler(commands=['3month'])
def handle_text(message):
    log(message)
    if SQLManager.getUserStrAttr(message, "status") == "events":
        FuncManager.showEvents(message, 3)
@bot.message_handler(commands=['6month'])
def handle_text(message):
    log(message)
    if SQLManager.getUserStrAttr(message, "status") == "events":
        FuncManager.showEvents(message, 6)
# menu /escape
@bot.message_handler(commands=['escape'])
def handle_text(message):
    log(message)
    if SQLManager.getUserStrAttr(message, "status") == "menu":
        FuncManager.comEscape(message)
# menu /search
@bot.message_handler(commands=['search'])
def handle_text(message):
    log(message)
    if SQLManager.getUserStrAttr(message, "status") == "menu":
        FuncManager.comSearch(message)
# menu /settings
@bot.message_handler(commands=['settings'])
def handle_text(message):
    log(message)
    if SQLManager.getUserStrAttr(message, "status") == "menu":
        FuncManager.comSettings(message)
# settings /set_city
@bot.message_handler(commands=['set_city'])
def handle_text(message):
    log(message)
    if SQLManager.getUserStrAttr(message, "status") == "settings":
        bot.send_message(message.chat.id, "Input your Home City")
        SQLManager.setUserStrAttr(message, "status", "set_city")
# menu /recommendations
@bot.message_handler(commands=['recommendations'])
def handle_text(message):
    log(message)
    if SQLManager.getUserStrAttr(message, "status") == "menu":
        FuncManager.comRecs(message)
# menu /feedback
@bot.message_handler(commands=['feedback'])
def handle_text(message):
    log(message)
    if SQLManager.getUserStrAttr(message, "status") == "menu":
        FuncManager.comFeed(message)
# feedback /airlines
@bot.message_handler(commands=['airlines'])
def handle_text(message):
    log(message)
    if SQLManager.getUserStrAttr(message, "status") == "feedback":
        bot.send_message(message.chat.id, "About which airline?")
        SQLManager.setUserStrAttr(message, "status", "feed-air")
# feedback /airlines
@bot.message_handler(commands=['cities'])
def handle_text(message):
    log(message)
    if SQLManager.getUserStrAttr(message, "status") == "feedback":
        bot.send_message(message.chat.id, "About which city?")
        SQLManager.setUserStrAttr(message, "status", "feed-cit")
# Usual text
@bot.message_handler(content_types=['text'])
def handle_text(message):
    log(message)
    KeyboardManager.analyzeAnswer(message)

bot.polling(none_stop=True)
