#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import csv
import tweepy
import sys
import re
import io
import time


bearer_token = \
    'AAAAAAAAAAAAAAAAAAAAANmAkAEAAAAAWuPFg8KhNybzTq3zzdgVytqT2SE%3DomchfegoeuBmkPFvTKhTUzj0QoLfVgtEmdya06BRzzacbc35dw'


def create_dataset(bearer_token, tweet_id):

    # Initializing Tweepy API

    client = tweepy.Client(bearer_token,wait_on_rate_limit= True)

    # Name of csv file to be created

    fname = 'latest-100-retweeter'

    # Open the spreadsheet

    with open('%s.csv' % fname, 'w', encoding='utf-8') as file:
        w = csv.writer(file)

        # Write header row (feature column names of your choice)

        w.writerow(['Time', 'Name', 'Username'])

        # For each tweet matching hashtag, write relevant info to the spreadsheet
        try:
            for tweet in tweepy.Paginator(client.get_retweeters, tweet_id,user_fields=["created_at"],
                    max_results=100).flatten(limit=100):
                w.writerow([tweet.created_at, tweet.name, tweet.username])

        except tweepy.RateLimitError as exc:
                   print('Rate limit!')
        except:
            e = sys.exc_info()[0]
            print("Error: %s" % e)
            print("error.")

# Enter your tweet_id here

tweet_id = 1593043381906993152

if __name__ == '__main__':
    create_dataset(bearer_token, tweet_id)
