#Program to extract ids of the followers of a given Twitter account.

from tweepy import OAuthHandler
import tweepy
import json
import ast
import pickle
import datetime as dt
import time, os
import pandas as pd

access_token = "XXXX"
access_token_secret = "XXXX"
consumer_key = "XXXX"
consumer_secret = "XXXX"


if __name__ == '__main__':

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)


    API = tweepy.API(auth)
    newsOrgs = ['aajtak', 'abpnewstv']

    for newsOrg in newsOrgs:
        cursor = -1
        while cursor != 0:
            try:
                ids = API.followers_ids(screen_name=newsOrg, cursor = cursor)
                if ids:
                    with open('FollowerIds/' + newsOrg + '.txt', 'a') as f:
                        f.write(str(ids))
                        f.write("\n")
                cursor = ids[1][1]

            except tweepy.RateLimitError:
                print('exception raised, waiting 15 minutes')
                print('(until:', dt.datetime.now()+dt.timedelta(minutes=15), ')')
                time.sleep(15*60)

            except tweepy.TweepError:
                pass    #passing because error took place because of internet disconnections