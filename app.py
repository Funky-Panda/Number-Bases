from flask import Flask, request, jsonify , redirect
import datetime
import json
import urllib.parse
from discord_webhook import DiscordWebhook
from time import sleep
from dotenv import load_dotenv
import os
import main


app = Flask(__name__)
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response
    
@app.route('/backend')
def receive_data():
    number = int(request.args.get('number'))
    actualBase = int(request.args.get('actualBase'))
    base = int(request.args.get('base'))
    answer , working = main.convertBinary(number,actualBase,base)
    print(answer,working)
    response = {'answer': answer,'working': working}

    return jsonify(response)

if __name__ == '__main__':
    app.run(port=8482)