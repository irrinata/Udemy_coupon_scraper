**About:**

A python telegram bot that scrapes infomation about fresh free Udemy coupons content from couponscorpion.com and sends it to teleram channel https://t.me/scudemy.
To prevent sending same coupon twice it adds all new records into a database and stores them for a month.

**Usage: main.py token chat**

You will need your own token and channel or chat to run it.

    positional arguments:
    token   Telegram bot token
    chat    Telegram chat id

**Requirements:**

requests
beautifulsoup4
pyTelegramBotAPI
lxml