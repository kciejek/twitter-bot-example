import requests
import urllib2
import time
from bs4 import BeautifulSoup
import random
import tweepy

consumer_key = ''
consumer_token = ''
access_token = ''
access_token_secret = '' 

auth = tweepy.OAuthHandler(consumer_key, consumer_token)    
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

url = 'http://bash.org.pl/browse/?page=1'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
posts = soup.findAll('div', {'class':'post-content'})
tweet = posts[random.randrange(len(posts))].text.strip()
print(tweet)

api.update_status(tweet);

