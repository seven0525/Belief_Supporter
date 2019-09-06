# -*- coding: UTF-8 -*-
import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask import send_from_directory
from base64 import b64encode
from sys import argv
import json
import requests
from io import BytesIO
import google_cva as google_cva
import extract_nutrition as extract_nutrition

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg','JPG'])

def judge_arabia(string):
    taboo_list = ["豚","酒","アルコール","みりん","醤油",
                  "ポーク","ラム","ゼラチン","ワイン","ウイスキー","ラード"]
    j = 0
    filtered_words = []
    for word in taboo_list:
        if word in string:
            j += 1
            # word = translator.translate(word)
            filtered_words.append(word)
    if j>=1:
        return "red", filtered_words
    else:
        return "silver", filtered_words

def judge_india(string):
    taboo_list = ["牛","ビーフ"]
    j = 0
    filtered_words = []
    for word in taboo_list:
        if word in string:
            # word = translator.translate(word)
            j += 1
            filtered_words.append(word)
    if j>=1:
        return "red", filtered_words
    else:
        return "silver", filtered_words

def judge_vege(string):
    taboo_list = ["肉","ハム","ソーセージ","ベーコン","ミート","動物","海老"]
    j = 0
    filtered_words = []
    for word in taboo_list:
        if word in string:
            j += 1
            # word = translator.translate(word)
            filtered_words.append(word)
    if j>=1:
        return "red", filtered_words
    else:
        return "silver", filtered_words



@app.route('/')
def index():
    return render_template('camera.html')


@app.route('/post', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        img_url_1 = request.form['image']
        img_url = img_url_1.split(",")[1]
        texts =  google_cva.main(img_url)
        print(texts)
        edited_text = extract_nutrition.edit(texts)
        arabia_color, arabia_words = judge_arabia(edited_text)
        india_color, india_words = judge_india(edited_text)
        vege_color, vege_words = judge_vege(edited_text)
        results_color = [arabia_color, india_color, vege_color]
        words = [arabia_words, india_words, vege_words]
        columns, values = extract_nutrition.main(edited_text)
        return render_template('result.html', color=results_color, words=words, results=texts, columns=columns, values=values)

if __name__ == '__main__':
    app.debug = True
    # app.run(host='0.0.0.0', ssl_context=('open_ssl/server.crt', 'open_ssl/server.key'), threaded=True, debug=True)
    app.run(host='0.0.0.0', ssl_context=('open_ssl/server.crt', 'open_ssl/server.key'))
