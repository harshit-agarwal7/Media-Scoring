""" Converting the ids of Twitter users to their handles. Ex - 122334343432 is converted to @starts_n_moon"""

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
	


	df = pd.read_csv("1.csv", dtype=object)		# 1.csv contains the ids whose twitter handles we want.

	ids = df["Id"].tolist()
	lenIds = len(ids)

	i = 0
	for j in range(19): #1900 users, can only get 100 users at a time.
		print(j)
		if (i+100 < lenIds):
			user_objs = API.lookup_users(user_ids=ids[i:i+100])
		else:
			user_objs = API.lookup_users(user_ids=ids[i:lenIds])

		for user in user_objs:
			idx = df.index[(df['Id'] == str(user.id))].tolist()[0]
			if (pd.isnull(df.loc[idx, 'Label'])):
				df.at[idx, 'Label'] = user.screen_name
		i = i + 100
		df.to_csv('Latest1.csv', index=False)
	

