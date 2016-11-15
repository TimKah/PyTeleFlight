import telebot
import constants
import DBManager

bot = telebot.TeleBot(constants.token)
db = DBManager.DBManager()
db_users = db.executeSQL("SELECT user_id, status from users")
from_city = ""

def findUser(message):
    ans = db.executeSQL("SELECT count(*) from users where user_id={0}")
    if ans == 0: 
        db.executeSQL("INSERT INTO users (user_id, firstname, lastname, login, password, city, permanent_country, status)"
                      "VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')".format(
                          message.chat.id, message.chat.first_name, message.chat.last_name, '','','','','start'))
def setStatus(message, status):
    db.executeSQL("UPDATE users SET status = '{0}' where user_id={1}".format(status, message.chat.id))
def getStatus(message):
    status = db.executeSQL("SELECT status from users where user_id = {0}".format(message.chat.id))
    return status[0][0]
def showMenu(message):
    setStatus(message, "menu")
    bot.send_message(message.chat.id, "Hi, {0}!\nWelcome to our Flights Search Bot!".format(message.chat.first_name))
    bot.send_message(message.chat.id, "Please, choose /start to get to menu")
    bot.send_message(message.chat.id, "Menu:\n/escape\n/search\n/recommendations\n\n/feedback\n/settings\n\nMade by Dilyara (@Akhsanova) & Timur (@TimKah)")
def searchFlight(message, user):
    if getStatus(message) == "menu":
        bot.send_message(message.chat.id, "Input departure city")
        setStatus(message, "search_1")
    elif getStatus(message) == "search_1":
        from_city = message.text
        bot.send_message(message.chat.id, "Input arrival city")
        setStatus(message, "search_2")
    elif getStatus(message) == "search_2":
        bot.send_message(message.chat.id, "Sorry, but Dilyara still working on it :(")
        if message.chat.id == 130396179:
            bot.send_message(message.chat.id, "Hi, Dilyara! :)")
        setStatus(message, "menu")
        showMenu(message, user)
def log(message):
    print("{0} {1} (#{2}) said \"{3}\"".format(message.chat.first_name, message.chat.last_name, message.chat.id, message.text))

@bot.message_handler(commands=['start'])
def handle_text(message):
    log(message)
    findUser(message)
    showMenu(message)
# menu /escape
@bot.message_handler(commands=['escape'])
def handle_text(message):
    log(message)
    findUser(message)
    if getStatus(message) == "menu":
        bot.send_message(message.chat.id, "This function can help you to find all cities which available from your city!")
        #if users[ans].city == "":
        #    bot.send_message(message.chat.id, "Unfortunately you can't this function till you set you Home City")
        #else:
        #    bot.send_message(message.chat.id, "OK")
        showMenu(message)
# menu /search
@bot.message_handler(commands=['search'])
def handle_text(message):
    log(message)
    findUser(message)
    if getStatus(message) == "menu":
        searchFlight(message)
# menu /settings
@bot.message_handler(commands=['settings'])
def handle_text(message):
    log(message)
    findUser(message)
    if getStatus(message) == "menu":
        setStatus(message, "settings")
        bot.send_message(message.chat.id, "/set_city - Set Home City\n\n/start - Back to Menu")
# settings /set_city
@bot.message_handler(commands=['set_city'])
def handle_text(message):
    log(message)
    findUser(message)
    if getStatus(message) == "settings":
        bot.send_message(message.chat.id, "Input your Home City")
        setStatus(message, "set_city")
# menu /recommendations
@bot.message_handler(commands=['recommendations'])
def handle_text(message):
    log(message)
    findUser(message)
    if getStatus(message) == "menu":
        bot.send_message(message.chat.id, "RECS")
        showMenu(message)
# menu /feedback
@bot.message_handler(commands=['feedback'])
def handle_text(message):
    log(message)
    findUser(message)
    if getStatus(message) == "menu":
        '''if len(users[ans].feedback) > 0:
            bot.send_message(message.chat.id, "Your last feedback: \"{0}\"".format(users[ans].feedback))
        bot.send_message(message.chat.id, "Please input your feedback".format(users[ans].city))
        setStatus(message, "feedback")'''
# Usual text
@bot.message_handler(content_types=['text'])
def handle_text(message):
    log(message)
    findUser(message)
    '''
    if getStatus(message) == "search_1" or getStatus(message) == "search_2":
        searchFlight(message)
    elif getStatus(message) == "set_city":
        users[ans].city = message.text
        bot.send_message(message.chat.id, "Home City set! Now your Home City is {0}".format(users[ans].city))
        showMenu(message, users[ans])
    elif getStatus(message) == "feedback":
        users[ans].feedback = message.text
        bot.send_message(message.chat.id, "Thank you for your feedback!".format(users[ans].city))
        showMenu(message, users[ans])'''

        
bot.polling(none_stop=True, interval=0)