import markovify
from twython import Twython
import random
from textblob import TextBlob, Word

#the twitter stuff

APP_KEY = ''
APP_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

twitter = Twython(APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

with open("strength.txt") as f:
	strength = f.read()

markov_strength = markovify.Text(strength)
strength_sentence = markov_strength.make_sentence()

if len(strength_sentence) < 140:
	result=strength_sentence
	twitter.update_status(status=result)