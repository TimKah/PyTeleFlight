﻿import telebot
import constants
import DBManager
import datetime

bot = telebot.TeleBot(constants.token)
db = DBManager.DBManager()
sql = "SELECT user_id, status from users"
db_users = db.executeSQL(sql)
from_city = []
feed = []


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
def leaveFeed(message, status):
    if status == "feed-cit" or status == "feed-air":
        if status == "feed-cit":
            ans = db.executeSQL("select city_id from cities where name = '{0}'".format(message.text))
        else:
            ans = db.executeSQL("select airlines_id from airlines where name = '{0}'".format(message.text))

        if len(ans) > 0:
            feed.append(constants.Feed(message.chat.id, ans[0][0]))
            setUserStrAttr(message, "status", "left-" + status)
            bot.send_message(message.chat.id, "So what you want to feedback?")
        else:
            if status == "feed-cit":
                bot.send_message(message.chat.id, "Where is no such city\n/start to get back to menu or try again")
            else:
                bot.send_message(message.chat.id, "Where is no such airline\n/start to get back to menu or try again")
    else:
        i = 0
        while (i < len(feed)):
            if feed[i].id == message.chat.id:
                break
            i += 1
        if status == "left-feed-cit":
            db.sendSQL("INSERT INTO citiesfeedback (text, grade, user_id, city_id) VALUES ('{0}',{1},{2},{3})".format(message.text, 5, feed[i].id, feed[i].name))
        else:
            db.sendSQL("INSERT INTO airlinesfeedback (text, grade, user_id, airlines_id) VALUES ('{0}',{1},{2},{3})".format(message.text, 5, feed[i].id, feed[i].name))
        bot.send_message(message.chat.id, "Thank you for your feedback!")
        del(feed[i])
        showMenu(message)
def showEvents(message, num):
    date = datetime.date.today()
    month = date.month
    day = date.day
    events = db.executeSQL("select c.name, e.name, e.day, e.month from events e join cities c on c.city_id = e.cities_id and"
    "(e.month = {0} AND e.day > {1}) OR (e.month = {2} AND e.day < {3}) OR (e.month > {0} AND e.month < {2})".format(
        month, day, month + num, day + 1))
    print(date)
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
# menu /events
@bot.message_handler(commands=['events'])
def handle_text(message):
    log(message)
    if getUserStrAttr(message, "status") == "menu":
        bot.send_message(message.chat.id, "This function can help you to find all special events all over the world!\n\n You can check for /1month, for /3month and for /6month")
        setUserStrAttr(message, "status", "events")
# events /?month
@bot.message_handler(commands=['1month'])
def handle_text(message):
    log(message)
    if getUserStrAttr(message, "status") == "events":
        showEvents(message, 1)
@bot.message_handler(commands=['3month'])
def handle_text(message):
    log(message)
    if getUserStrAttr(message, "status") == "events":
        showEvents(message, 3)
@bot.message_handler(commands=['6month'])
def handle_text(message):
    log(message)
    if getUserStrAttr(message, "status") == "events":
        showEvents(message, 6)
# menu /escape
@bot.message_handler(commands=['escape'])
def handle_text(message):
    log(message)
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
    if getUserStrAttr(message, "status") == "menu":
        searchFlight(message)
# menu /settings
@bot.message_handler(commands=['settings'])
def handle_text(message):
    log(message)
    if getUserStrAttr(message, "status") == "menu":
        setUserStrAttr(message, "status", "settings")
        bot.send_message(message.chat.id, "/set_city - Set Home City\n\n/start - Back to Menu")
# settings /set_city
@bot.message_handler(commands=['set_city'])
def handle_text(message):
    log(message)
    if getUserStrAttr(message, "status") == "settings":
        bot.send_message(message.chat.id, "Input your Home City")
        setUserStrAttr(message, "status", "set_city")
# menu /recommendations
@bot.message_handler(commands=['recommendations'])
def handle_text(message):
    log(message)
    if getUserStrAttr(message, "status") == "menu":
        bot.send_message(message.chat.id, "RECS")
        showMenu(message)
# menu /feedback
@bot.message_handler(commands=['feedback'])
def handle_text(message):
    log(message)
    if getUserStrAttr(message, "status") == "menu":
        bot.send_message(message.chat.id, "Do you want leave feedback about /airlines or /cities?")
        setUserStrAttr(message, "status", "feedback")
        '''if len(users[ans].feedback) > 0:
            bot.send_message(message.chat.id, "Your last feedback: \"{0}\"".format(users[ans].feedback))
        bot.send_message(message.chat.id, "Please input your feedback".format(users[ans].city))
        setStatus(message, "feedback")'''
# feedback /airlines
@bot.message_handler(commands=['airlines'])
def handle_text(message):
    log(message)
    if getUserStrAttr(message, "status") == "feedback":
        bot.send_message(message.chat.id, "About which airline?")
        setUserStrAttr(message, "status", "feed-air")
# feedback /airlines
@bot.message_handler(commands=['cities'])
def handle_text(message):
    log(message)
    if getUserStrAttr(message, "status") == "feedback":
        bot.send_message(message.chat.id, "About which city?")
        setUserStrAttr(message, "status", "feed-cit")
# Usual text
@bot.message_handler(content_types=['text'])
def handle_text(message):
    log(message)
    status = getUserStrAttr(message,"status")
    if status == "search_1" or status == "search_2":
        searchFlight(message)
    elif status == "set_city":
        new_city = db.executeSQL("SELECT city_id from cities where name = '{0}'".format(message.text))
        setUserNumAttr(message,"city", new_city[0][0])
        bot.send_message(message.chat.id, "Home City set! Now your Home City is {0}".format(message.text))
        showMenu(message)
    elif status == "escape":
        city_from = db.executeSQL("SELECT cities.name from cities where city_id = {0}".format(getUserNumAttr(message, "city")))
        showFlight(message, city_from[0][0],message.text)
    elif status == "feed-air" or status == "feed-cit":
        leaveFeed(message, status)
    elif status == "left-feed-air" or status == "left-feed-cit":
        leaveFeed(message, status)



bot.polling(none_stop=True, interval=0)
