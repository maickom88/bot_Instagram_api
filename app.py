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
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#PARTE2

app = Flask(__name__)

@app.route('/')
def nao_entre_em_panico():
    if request.headers.get('Authorization') == '42':
        return jsonify({"42": "a resposta para a vida, o universo e tudo mais"})
    return jsonify({"message": "Não entre em pânico!"})

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

@app.route("/string", methods=["POST, GET"])
def resString():
    if request.method == 'POST':
        stringName = request.form.get('name')
        stringSecondeName = request.form['secondName']
        return stringName
    return jsonify(stringName)
#PARTE4
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
