import telebot
import config

bot = telebot.TeleBot(config.BOT_TOKEN, parse_mode="HTML")


if __name__ == "__main__":

    from menu import send_to_admin
    send_to_admin()


