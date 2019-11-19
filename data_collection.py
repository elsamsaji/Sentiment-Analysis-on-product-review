# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 22:11:17 2019

@author: Elizabeth
"""

import tweepy
#import nltk
from textblob import Textblob

consumer_key = 'j3h9uEE4KemCKwp5g8MUGLf8d'
consumer_secret = 'mQvUU7bGQ4gSB3QPy2WJCzgSEBBwOrvuo7nR92zQIjmJUZvypd'

access_token = '1156462652077400064-7GLxte1Rr3Ml62r8L79lYgS3Pz9GuL' 
access_token_secret = '8zBkNG1fLNel6w4hVJw5j2PJQ6ReGbqKI4Tgyd64E6rLE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
public_tweets = api.search( 'samsungs10' )

for tweet in public_tweets:
    print(tweet.text)
    analysis = Textblob (tweet.text)
    print(analysis.sentiment)