from flask import Flask, jsonify, request
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import time
import json
import getpass
import getpass_ak
from bot_insta import bot_instagram
from celery import Celery
from multiprocessing import Process
#PARTE2
broker_url = 'amqp://guest@localhost'          # Broker URL for RabbitMQ task queue

app = Flask(__name__)
celery = Celery(app.name, broker=broker_url)

@celery.task(bind=True)
def bot(self, username, password, userinsta ):
    bot = bot_instagram.InstagramBot(username, password, userinsta)
    numberClicks = bot.getProfile()
    return numberClicks


@app.route('/')
def nao_entre_em_panico():
    if request.headers.get('Authorization') == '42':
        return jsonify({"42": "a resposta para a vida, o universo e tudo mais"})
    return jsonify({"message": "Não entre em pânico!"})

#PARTE3

@app.route("/instaBot3", methods=["GET"])
def followProfille3():
    username = request.args['name']
    password = request.args['password']
    userinsta = request.args['userinsta']
    heavy_process = Process(  # Create a daemonic process with heavy "my_func"
        target= botP(username, password, userinsta),
        daemon=True
    )
    heavy_process.start()
    numberClicks = 'ok'

    return jsonify(numberClicks)
@app.route("/instaBot2", methods=["GET"])
def followProfille2():
    username = request.args['name']
    password = request.args['password']
    userinsta = request.args['userinsta']
    numberClicks = bot(username, password, userinsta)
    print(numberClicks)

    return jsonify(numberClicks)


@app.route("/instaBot", methods=["POST"])
def followProfille1():
    username = request.json['name']
    password = request.json['password']
    userinsta = request.json['userinsta']
    bot = bot_instagram.InstagramBot(username, password, userinsta)
    numberClicks = bot.getProfile()
    print(numberClicks)

    return jsonify(numberClicks)


@app.route("/instaBotFollow", methods=["GET"])
def followProfille():
    username = request.args['name']
    password = request.args['password']
    userinsta = request.args['userinsta']
    bot = bot_instagram.InstagramBot(username, password, userinsta)
    numberClicks = bot.getProfile()
    print(login)

    return jsonify(login)

@app.route("/instaCommentAllFeed", methods=["GET"])
def commentAllPost():
    username = request.args['name']
    password = request.args['password']
    userinsta = request.args['userinsta']
    comment = request.args['comment']
    limit = request.args['limit']
    limit = int(limit)
    bot = bot_instagram.InstagramBot(username, password, userinsta)
    quantComment = bot.commentPost(comment, limit)
    print(quantComment)

    return jsonify(quantComment)

@app.route("/string", methods=["POST"])
def resString():
    if request.method == 'POST':
        username = request.json['name']
        password = request.json['password']
        userinsta = request.args['userinsta']
        comment = request.args['comment']
        limit = request.args['limit']
        limit = int(limit)
        bot = bot_instagram.InstagramBot(username, password, userinsta)
        quantComment = bot.commentPost(comment, limit)
        print(quantComment)

    return jsonify(quantComment)


def botP(username, password, userinsta):
    bot = bot_instagram.InstagramBot(username, password, userinsta)
    numberClicks = bot.getProfile()

#PARTE4
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
