import telebot
import SQLManager
import FuncManager
import constants

bot = telebot.TeleBot(constants.token)

def getMainMenu():
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)

    markup.row('Escape', 'Events', 'Search')
    markup.row('Recommendations', 'Feedback')
    markup.row('Settings', 'Authors')

    return markup
def analyzeAnswer(message):
    status = SQLManager.getUserStrAttr(message, "status")
    if status == "menu":
        message.text = {
            "Escape": FuncManager.comEscape(message),
            "Events": FuncManager.comEvents(message),
            "Search": FuncManager.comSearch(message),
            "Recommendations": FuncManager.comRecs(message),
            "Feedback": FuncManager.comFeed(message),
            "Settings": FuncManager.comSettings(message),
            "Authors": FuncManager.comAuthors(message)
        }
    elif status == "search_1" or status == "search_2":
        FuncManager.searchFlight(message)
    elif status == "set_city":
        new_city = SQLManager.db.executeSQL("SELECT city_id from cities where name = '{0}'".format(message.text))
        SQLManager.setUserNumAttr(message, "city", new_city[0][0])
        bot.send_message(message.chat.id, "Home City set! Now your Home City is {0}".format(message.text))
        FuncManager.showMenu(message)
    elif status == "escape":
        city_from = SQLManager.db.executeSQL(
            "SELECT cities.name from cities where city_id = {0}".format(SQLManager.getUserNumAttr(message, "city")))
        FuncManager.showFlight(message, city_from[0][0], message.text)
    elif status == "feed-air" or status == "feed-cit":
        FuncManager.leaveFeed(message, status)
    elif status == "left-feed-air" or status == "left-feed-cit":
        FuncManager.leaveFeed(message, status)