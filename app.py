import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask import send_from_directory
from base64 import b64encode
from sys import argv
import json
import requests
from io import BytesIO
from PIL import Image
import google_cva as google_cva

app = Flask(__name__)

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg','JPG', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('camera.html')


@app.route('/post', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        img_url_1 = request.form['image']
        img_url = img_url_1.split(",")[1]
        texts =  google_cva.main(img_url)
        #texts = "Hello!"
        return render_template('result.html', img_url=img_url_1, texts=texts)
        

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.debug = True
    app.run()