import requests
from bs4 import BeautifulSoup
import sqlite3
import telebot
import argparse

# This is the code for my personal bot posting to the https://t.me/scudemy telegram channel.
# Feel free to subscribe to the channel if you would like to receive information about fresh
# coupons or check out the bot operation in production.

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('token', help='Telegram bot token')
parser.add_argument('chat', help='Telegram chat id')
args = parser.parse_args()

# Telegram Bot
bot = telebot.TeleBot(args.token)

# Database
db = sqlite3.connect('couponscorpion.db')
cur = db.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS coupon(
    url TEXT,
    timestamp INTEGER
)""")
db.commit()

# Coupon website scraper
url = 'https://couponscorpion.com/'
coupons = BeautifulSoup(requests.get(url).text, 'lxml')
couponsurl = [x.a.get('href') for x in coupons.findAll('h3', class_="flowhidden mb10 fontnormal position-relative")]

for i in couponsurl:
    cur.execute("SELECT count(*) FROM coupon WHERE url = ?", (i,))
    if (cur.fetchall()[0][0]) == 0:
        # Sending to telegram channel
        bot.send_message(args.chat, i)
        # Adding database record
        cur.execute("INSERT INTO coupon (url, timestamp) VALUES (?, strftime('%s','now'))", (i,))
        db.commit()

# Deleting ald records
cur.execute("DELETE FROM coupon WHERE timestamp < strftime('%s','now') - 30*24*60*60")
db.commit()
