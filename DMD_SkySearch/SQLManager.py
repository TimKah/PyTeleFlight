import telebot
import constants
import DBManager

bot = telebot.TeleBot(constants.token)
db = DBManager.DBManager()
sql = "SELECT user_id, status from users"
db_users = db.executeSQL(sql)
from_city = []
feed = []

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