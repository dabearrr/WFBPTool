#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from twython import Twython

import json
#import pandas as pd
#import matplotlib.pyplot as plt

#Variables that contains the user credentials to access Twitter API
access_token = "1609942975-s7M7XaIQHL4j4dpk1SAKhczezrMjsGK5x5i4Jg1"
access_token_secret = "obmSNYTpgzzhTzpA28l9hdPDvt0gvfi9MwH3mRftHNAIA"
consumer_key = "b5Gec7Y5CtrC68XilifFJqgGV"
consumer_secret = "O4ctVb2uQ6DKSdNm2qGYCVSWUFdo7zLSkviv1HOlup45FwHEUK"

#string we are filtering by
filterString = ['vauban chassis', 'nitain extract', 'warframe', 'bernie']

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=filterString)

    twitter = Twython(APP_KEY, APP_SECRET
    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    twitter.update_status(status='See how easy using Twython is!')