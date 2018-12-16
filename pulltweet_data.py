#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 15:58:14 2018

@author: john
"""

from flask import Flask, render_template
from flask import request
from jinja2 import Template
import tweepy
import json
import datetime
from datetime import datetime

APP_KEY = 'MWQadaodeKZ02JKLfkJA8OhF9'  # Customer Key here
APP_SECRET = 'hVGVTiEtAEFwzLZLB6gpa8IaI2xrdv9l4G7S61AbcI3lrPwcU3'  # Customer secret here
OAUTH_TOKEN = '2942702198-rybhZK6kteq3c1KyIoXXLtV3C49Q8LlW2VkQcz5'  # Access Token here
OAUTH_TOKEN_SECRET = 'ErFaebAlbAfL1e4yh2NjEx1VBCFQq8En6OurUbHYyUKKY'  # Access Token Secret here

app = Flask(__name__, template_folder="mytemplate")

@app.route('/twitter', methods=['GET'])
def twitter():
    all_tweets_text = []
    name = request.args.get('name') #if key doesn't exist, returns None
    sdate = datetime.strptime(request.args.get('sdate'), '%Y-%m-%d')
    edate = datetime.strptime(request.args.get('edate'), '%Y-%m-%d')
    auth = tweepy.OAuthHandler(APP_KEY, APP_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

    api = tweepy.API(auth)
    public_tweets = api.user_timeline(screen_name=name, tweet_mode='extended')
    
    for tweet_info in public_tweets:   
        if tweet_info.created_at < edate and tweet_info.created_at > sdate:
           all_tweets_text.append(tweet_info.full_text)
           
    return render_template('pulltweet_data.html', data=all_tweets_text)
       
if(__name__) == '__main__':
    app.run(debug=True)  