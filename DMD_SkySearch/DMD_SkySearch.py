import telebot
import constants
import DBManager

bot = telebot.TeleBot(constants.token)
db = DBManager.DBManager("25655")

users = []

def findUser(message):
    i = 0
    while i < len(users):
        if message.chat.id == users[i].id:
            return i
        i += 1
    print("User {0} not found".format(message.chat.id))
    createUser(message)
    return findUser(message)
def createUser(message):
    new_user = constants.User(message.chat.id, "start")
    users.append(new_user)
    print("User created: {0} {1} #{2}".format(message.chat.first_name, message.chat.last_name, message.chat.id))
    bot.send_message(message.chat.id, "Hi, {0}!\nWelcome to our Flights Search Bot!".format(message.chat.first_name))
    bot.send_message(message.chat.id, "Please, choose /start to get to menu")
    return len(users) - 1
def showMenu(message, user):
    user.status = "menu"
    bot.send_message(message.chat.id, "Menu:\n/escape\n/search\n/recommendations\n\n/feedback\n/settings\n\nMade by Dilyara (@Akhsanova) & Timur (@TimKah)")
def searchFlight(message, user):
    if user.status == "menu":
        bot.send_message(message.chat.id, "Input departure city")
        user.status = "search_1"
    elif user.status == "search_1":
        user.from_city = message.text
        bot.send_message(message.chat.id, "Input arrival city")
        user.status = "search_2"
    elif user.status == "search_2":
        bot.send_message(message.chat.id, "Sorry, but Dilyara still working on it :(")
        if message.chat.id == 130396179:
            bot.send_message(message.chat.id, "Hi, Dilyara! :)")
        user.status = "menu"
        showMenu(message, user)
def log(message):
    print("{0} {1} (#{2}) said \"{3}\"".format(message.chat.first_name, message.chat.last_name, message.chat.id, message.text))

@bot.message_handler(commands=['start'])
def handle_text(message):
    log(message)
    ans = findUser(message)
    showMenu(message, users[ans])
# menu /escape
@bot.message_handler(commands=['escape'])
def handle_text(message):
    log(message)
    ans = findUser(message)
    if users[ans].status == "menu":
        bot.send_message(message.chat.id, "This function can help you to find all cities which available from your city!")
        if users[ans].city == "":
            bot.send_message(message.chat.id, "Unfortunately you can't this function till you set you Home City")
        else:
            bot.send_message(message.chat.id, "OK")
        showMenu(message, users[ans])
# menu /search
@bot.message_handler(commands=['search'])
def handle_text(message):
    ans = findUser(message)
    log(message)
    if users[ans].status == "menu":
        searchFlight(message, users[ans])
# menu /settings
@bot.message_handler(commands=['settings'])
def handle_text(message):
    log(message)
    ans = findUser(message)
    if users[ans].status == "menu":
        users[ans].status = "settings"
        bot.send_message(message.chat.id, "/set_city - Set Home City\n\n/start - Back to Menu")
# settings /set_city
@bot.message_handler(commands=['set_city'])
def handle_text(message):
    log(message)
    ans = findUser(message)
    if users[ans].status == "settings":
        bot.send_message(message.chat.id, "Input your Home City")
        users[ans].status = "set_city"
# menu /recommendations
@bot.message_handler(commands=['recommendations'])
def handle_text(message):
    log(message)
    ans = findUser(message)
    if users[ans].status == "menu":
        bot.send_message(message.chat.id, "RECS")
        showMenu(message, users[ans])
# menu /feedback
@bot.message_handler(commands=['feedback'])
def handle_text(message):
    log(message)
    ans = findUser(message)
    if users[ans].status == "menu":
        if len(users[ans].feedback) > 0:
            bot.send_message(message.chat.id, "Your last feedback: \"{0}\"".format(users[ans].feedback))
        bot.send_message(message.chat.id, "Please input your feedback".format(users[ans].city))
        users[ans].status = "feedback"
# Usual text
@bot.message_handler(content_types=['text'])
def handle_text(message):
    log(message)
    ans = findUser(message)
    if users[ans].status == "search_1" or users[ans].status == "search_2":
        searchFlight(message, users[ans])
    elif users[ans].status == "set_city":
        users[ans].city = message.text
        bot.send_message(message.chat.id, "Home City set! Now your Home City is {0}".format(users[ans].city))
        showMenu(message, users[ans])
    elif users[ans].status == "feedback":
        users[ans].feedback = message.text
        bot.send_message(message.chat.id, "Thank you for your feedback!".format(users[ans].city))
        showMenu(message, users[ans])

        
bot.polling(none_stop=True, interval=0)