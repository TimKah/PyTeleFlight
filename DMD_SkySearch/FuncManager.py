import telebot
import constants
import DBManager
import SQLManager
import KeyboardManager
import datetime

bot = telebot.TeleBot(constants.token)
db = DBManager.DBManager()
sql = "SELECT user_id, status from users"
db_users = db.executeSQL(sql)
from_city = []
feed = []

def comEscape(message):
    if SQLManager.getUserNumAttr(message, "city") == 0:
        bot.send_message(message.chat.id, "Unfortunately you can't this function till you set you Home City")
        showMenu(message)
    else:
        bot.send_message(message.chat.id, "This function can help you to find all cities which available from your city!")
        showCities(message)
def comEvents(message):
    bot.send_message(message.chat.id, "This function can help you to find all special events all over the world!\n\n You can check for /1month, for /3month and for /6month")
    SQLManager.setUserStrAttr(message, "status", "events")
def comSearch(message):
    searchFlight(message)
def comRecs(message):
    bot.send_message(message.chat.id, "RECS")
    showMenu(message)
def comFeed(message):
    bot.send_message(message.chat.id, "Do you want leave feedback about /airlines or /cities?")
    SQLManager.setUserStrAttr(message, "status", "feedback")
def comSettings(message):
    SQLManager.setUserStrAttr(message, "status", "settings")
    bot.send_message(message.chat.id, "/set_city - Set Home City\n\n/start - Back to Menu")
def comAuthors(message):
    showMenu(message)

def showCities(message):
    SQLManager.setUserStrAttr(message, "status", "escape")
    cities = db.executeSQL("SELECT DISTINCT cities.name from cities join flights on flights.city_from = {0} and flights.city_to = cities.city_id".format(
        SQLManager.getUserNumAttr(message, "city")))
    city_from = db.executeSQL("SELECT cities.name from cities where city_id = {0}".format(SQLManager.getUserNumAttr(message, "city")))
    msg = "Here is cities where you can go right from {0}:\n\n".format(city_from[0][0].replace(" ",""))
    j = 0
    while (j < len(cities)):
        msg += "{0}, ".format(cities[j][0].replace(" ",""))
        j += 1
    msg += "\n\nPress /start to return to Main Menu or type city to start search"
    bot.send_message(message.chat.id, msg)
def showMenu(message):
    SQLManager.setUserStrAttr(message, "status", "menu")
    bot.send_message(message.chat.id, "Hi, {0}!\nWelcome to our Flights Search Bot!\n\nMenu:\n/escape\n/events\n/search\n/recommendations\n\n/feedback\n/settings".format(message.chat.first_name))
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
    if SQLManager.getUserStrAttr(message, "status") == "menu":
        bot.send_message(message.chat.id, "Input departure city")
        SQLManager.setUserStrAttr(message, "status", "search_1")
    elif SQLManager.getUserStrAttr(message, "status") == "search_1":
        from_city.append(constants.City(message.chat.id, message.text))
        bot.send_message(message.chat.id, "Input arrival city")
        SQLManager.setUserStrAttr(message, "status", "search_2")
    elif SQLManager.getUserStrAttr(message, "status") == "search_2":
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
            SQLManager.setUserStrAttr(message, "status", "left-" + status)
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
            db.sendSQL("INSERT INTO citiesfeedback (text, grade, user_id, cities_id) VALUES ('{0}',{1},{2},{3})".format(message.text, 5, feed[i].id, feed[i].name))
        else:
            db.sendSQL("INSERT INTO airlinesfeedback (text, grade, user_id, airlines_id) VALUES ('{0}',{1},{2},{3})".format(message.text, 5, feed[i].id, feed[i].name))
        bot.send_message(message.chat.id, "Thank you for your feedback!")
        del(feed[i])
        showMenu(message)
def showEvents(message, num):
    date = datetime.date.today()
    month = int(date.strftime("%m"))
    day = int(date.strftime("%d"))
    print(month + num)
    if num + month > 12:
        events = db.executeSQL("select c.name, e.name, e.day, e.month from events e join cities c on c.city_id = e.cities_id and"
            "((e.month = {0} AND e.day > {1}) OR (e.month = {2} AND e.day < {3}) OR (e.month > {0} OR e.month < {2}))".format(
            month, day, month + num - 12, day + 1))
    else:
        events = db.executeSQL("select c.name, e.name, e.day, e.month from events e join cities c on c.city_id = e.cities_id and"
            "((e.month = {0} AND e.day > {1}) OR (e.month = {2} AND e.day < {3}) OR (e.month > {0} AND e.month < {2}))".format(
            month, day, month + num, day + 1))
    if len(events) == 0:
        bot.send_message(message.chat.id, "No events")
    else:
        i = 0
        msg = ""
        while (i < len(events)):
            happy = events[i][1].replace(' ','')
            happy = happy.replace('_',' ')
            msg += "{0}: {1} / {2}.{3}.{4}\n".format(events[i][0].replace(' ',''), happy, events[i][3], events[i][2], 2016 + round((month + num - 1) / 12))
            i += 1
        bot.send_message(message.chat.id, "We found this events:\n\n{0}".format(msg))
    print(len(events))
    showMenu(message)