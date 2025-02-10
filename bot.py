import tweepy
import telebot

# Configuración de Twitter
API_KEY = "E0SEAmi9TPAjIk6eEZY5PsJCV"
API_SECRET_KEY = "ZhQbAfcT77e8xEmNGR54oSmy2LjNOaw>
ACCESS_TOKEN = "1562434686319992836-7lu0ghNVJ8GgK>
ACCESS_TOKEN_SECRET = "vtW0vbyZx1cNhq3g0Q8pP34zYs>

# Configuración del bot de Telegram
TELEGRAM_BOT_TOKEN = "7019982517:AAGCdLDU79Oi4fF4>
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Clave secreta
CLAVE_SECRETA = "leonarDO:9405"

# Función para autenticar en Twitter
def autenticar_twitter():
    auth = tweepy.OAuthHandler(API_KEY, API_SECRE>
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TO>
    return tweepy.API(auth)
