import telebot
import constants
import DBManager

bot = telebot.TeleBot(constants.token)
db = DBManager.DBManager()
sql = "SELECT user_id, status from users"
db_users = db.executeSQL(sql)
from_city = []


# SQL shit
def findUser(message):
    ans = db.executeSQL("SELECT * from users where user_id={0}".format(message.chat.id))
    if len(ans) == 0: 
        db.sendSQL("INSERT INTO users (user_id, firstname, lastname, login, password, permanent_country, city, status) "
                   "VALUES ({0}, '{1}', '{2}', '{3}', '{4}', '{5}', {6}, '{7}');".format(
                       message.chat.id, message.chat.first_name, message.chat.last_name, None,None,None,0,'start'))
def setUserStrAttr(message, name, value):
    db.sendSQL("UPDATE users SET {0} = '{1}' where user_id={2}".format(name, value, message.chat.id))
def getUserStrAttr(message, name):
    ans = db.executeSQL("SELECT {0} from users where user_id = {1}".format(name, message.chat.id))
    return ans[0][0].replace(" ","")
def setUserNumAttr(message, name, value):
    db.sendSQL("UPDATE users SET {0} = {1} where user_id={2}".format(name, value, message.chat.id))
def getUserNumAttr(message, name):
    ans = db.executeSQL("SELECT {0} from users where user_id = {1}".format(name, message.chat.id))
    return ans[0][0]
# Other shit
def showCities(message):
    setUserStrAttr(message, "status", "escape")
    cities = db.executeSQL("SELECT DISTINCT cities.name from cities join flights on flights.city_from = {0} and flights.city_to = cities.city_id".format(
        getUserNumAttr(message, "city")))
    city_from = db.executeSQL("SELECT cities.name from cities where city_id = {0}".format(getUserNumAttr(message, "city")))
    msg = "Here is cities where you can go right from {0}:\n\n".format(city_from[0][0].replace(" ",""))
    j = 0
    while (j < len(cities)):
        msg += "{0}, ".format(cities[j][0].replace(" ",""))
        j += 1
    msg += "\n\nPress /start to return to Main Menu or type city to start search"
    bot.send_message(message.chat.id, msg)
def showMenu(message):
    setUserStrAttr(message, "status", "menu")
    bot.send_message(message.chat.id, "Hi, {0}!\nWelcome to our Flights Search Bot!".format(message.chat.first_name))
    bot.send_message(message.chat.id, "Please, choose /start to get to menu")
    bot.send_message(message.chat.id, "Menu:\n/escape\n/search\n/recommendations\n\n/feedback\n/settings\n\nMade by Dilyara (@Akhsanova) & Timur (@TimKah)")
def showFlight(message, city_from, city_to):
    fligts = db.executeSQL("SELECT f.city_to, f.city_from, f.date_start, f.date_end, f.duration, a.name "
        "FROM  flights f JOIN airlines a ON "
        "f.airlines_id = a.airlines_id "
        "AND f.city_to = (select city_id from cities where name = '{0}') "
        "AND f.city_from = (select city_id from cities where name = '{1}')".format(city_to,city_from))
    print("I found {0} fligts".format(len(fligts)))
    if len(fligts) > 0:
        msg = "We found {0} flights from {1} to {2}:\n\n".format(len(fligts), city_from, message.text)
        i = 0
        while (i < len(fligts)):
            msg += "Departure date: {0}\nArrival date: {1}\nDuration: {2} hours\nAirlines: {3}\n\n".format(fligts[i][2], fligts[i][3], fligts[i][4], fligts[i][5])
            i += 1
        msg += "Press /start to return to Main Menu"
        bot.send_message(message.chat.id, msg)
    else:
        bot.send_message(message.chat.id, "Unfortunately, there is no flight from {0} to {1}\n\nPress /start to return to Main Menu".format(city_from, message.text))
def searchFlight(message):
    if getUserStrAttr(message, "status") == "menu":
        bot.send_message(message.chat.id, "Input departure city")
        setUserStrAttr(message, "status", "search_1")
    elif getUserStrAttr(message, "status") == "search_1":
        from_city.append(constants.City(message.chat.id, message.text))
        bot.send_message(message.chat.id, "Input arrival city")
        setUserStrAttr(message, "status", "search_2")
    elif getUserStrAttr(message, "status") == "search_2":
        '''if message.chat.id == 130396179:
            bot.send_message(message.chat.id, "Hi, Dilyara! :)")'''
        print(len(from_city))
        if (len(from_city) > 0):
            i = 0
            while (i < len(from_city)):
                if from_city[i].id == message.chat.id:
                    break
                i += 1
            showFlight(message,from_city[i].name,message.text)
            del(from_city[i])
        else:
            bot.send_message(message.chat.id, "Che-to kosyak :/")
            showMenu(message)
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
    findUser(message)
    showMenu(message)
# menu /escape
@bot.message_handler(commands=['escape'])
def handle_text(message):
    log(message)
    findUser(message)
    if getUserStrAttr(message, "status") == "menu":
        bot.send_message(message.chat.id, "This function can help you to find all cities which available from your city!")
        if getUserNumAttr(message, "city") == 0:
            bot.send_message(message.chat.id, "Unfortunately you can't this function till you set you Home City")
            showMenu(message)
        else:
            showCities(message)
# menu /search
@bot.message_handler(commands=['search'])
def handle_text(message):
    log(message)
    findUser(message)
    if getUserStrAttr(message, "status") == "menu":
        searchFlight(message)
# menu /settings
@bot.message_handler(commands=['settings'])
def handle_text(message):
    log(message)
    findUser(message)
    if getUserStrAttr(message, "status") == "menu":
        setUserStrAttr(message, "status", "settings")
        bot.send_message(message.chat.id, "/set_city - Set Home City\n\n/start - Back to Menu")
# settings /set_city
@bot.message_handler(commands=['set_city'])
def handle_text(message):
    log(message)
    findUser(message)
    if getUserStrAttr(message, "status") == "settings":
        bot.send_message(message.chat.id, "Input your Home City")
        setUserStrAttr(message, "status", "set_city")
# menu /recommendations
@bot.message_handler(commands=['recommendations'])
def handle_text(message):
    log(message)
    findUser(message)
    if getUserStrAttr(message, "status") == "menu":
        bot.send_message(message.chat.id, "RECS")
        showMenu(message)
# menu /feedback
@bot.message_handler(commands=['feedback'])
def handle_text(message):
    log(message)
    findUser(message)
    if getUserStrAttr(message, "status") == "menu":
        '''if len(users[ans].feedback) > 0:
            bot.send_message(message.chat.id, "Your last feedback: \"{0}\"".format(users[ans].feedback))
        bot.send_message(message.chat.id, "Please input your feedback".format(users[ans].city))
        setStatus(message, "feedback")'''
# Usual text
@bot.message_handler(content_types=['text'])
def handle_text(message):
    log(message)
    findUser(message)
    if getUserStrAttr(message,"status") == "search_1" or getUserStrAttr(message,"status") == "search_2":
        searchFlight(message)
    elif getUserStrAttr(message,"status") == "set_city":
        new_city = db.executeSQL("SELECT city_id from cities where name = '{0}'".format(message.text))
        setUserNumAttr(message,"city", new_city[0][0])
        bot.send_message(message.chat.id, "Home City set! Now your Home City is {0}".format(message.text))
        showMenu(message)
    elif getUserStrAttr(message,"status") == "feedback":
        '''users[ans].feedback = message.text
        bot.send_message(message.chat.id, "Thank you for your feedback!".format(users[ans].city))'''
        showMenu(message)
    elif getUserStrAttr(message,"status") == "escape":
        city_from = db.executeSQL("SELECT cities.name from cities where city_id = {0}".format(getUserNumAttr(message, "city")))
        showFlight(message, city_from[0][0],message.text)

bot.polling(none_stop=True, interval=0)
