#PARTE1
from flask import Flask, jsonify, request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import os
import time
import json
import getpass
import getpass_ak
from bot_insta import bot_instagram
#PARTE2

app = Flask(__name__)
#PARTE3
@app.route("/instaBotFollow", methods=["GET"])
def followProfille():
    username = request.args['name']
    password = request.args['password']
    userinsta = request.args['userinsta']
    msg = "You passed {} args using query string. Your args: {}".format(len(request.args), [username, password, userinsta])
    time.sleep(1)
    bot = bot_instagram.InstagramBot(username, password, userinsta)
    login = bot.login()
    numberClicks = bot.getProfile()
    bot.close()
    bot.quit()
    time.sleep(5)
    print(numberClicks)

    return jsonify(numberClicks)

@app.route("/instaCommentAllFeed", methods=["GET"])
def commentAllPost():
    uusername = request.args['name']
    password = request.args['password']
    userInsta = request.args['userinsta']
    comment = request.args['comment']
    quantComment = bot.commentPost(username, password, userInsta, comment)
    time.sleep(3)
    bot.close()
    bot.quit()
    print(quantComment)

    return jsonify(quantComment)

@app.route("/string", methods=["GET"])
def resString():
    string = request.args['str']
    print(string)

    return jsonify(string)
#PARTE4
if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='127.0.0.1', port=port)
