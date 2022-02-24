from passwords import *
import numpy as np
import tweepy
import json
import pandas as pd
import time
import pytz
from datetime import date, time, datetime
#tokens are hiden
def getClient():
    client=tweepy.Client(bearer_token=bearer_token,
                         consumer_key=consumer_key,
                         consumer_secret=consumer_secret,
                         access_token=access_token,
                         access_token_secret=access_token_secret,
                         wait_on_rate_limit=True)
    
    return client
    
def loop_userTweets(data_df):
    resultsTweets_pd=pd.DataFrame()
    for index, row in data_df.iterrows():
        #for userId in conjunto:
        results_tweets2=getTweets1_total_user(userId = data_df.loc[index,'userId'],
                                  var_username = data_df.loc[index,'Twitterhandle'],
                                  start_time_value = data_df.loc[index,'start_time_value'],
                                 end_time_value = data_df.loc[index,'end_time_value'],
                                 country = data_df.loc[index,'Country_code'],
                                 election_year = data_df.loc[index,'Electionyear'],
                                             descrip=data_df.loc[index,'description'])
        resultsTweets_pd=resultsTweets_pd.append(results_tweets2)
            
    return resultsTweets_pd

def getTweets1_total_user(userId,var_username,start_time_value,end_time_value,country,election_year,descrip):
    print(var_username)
    utc=pytz.UTC
    results_tweets = pd.DataFrame().copy()
    names_columns=['country','election_year','username','userId','userDescription','start_time','end_time','id','text','created_at','retweet_count','reply_count','like_count','quote_count']
    obj = {k: [] for k in names_columns}
    s_year=int(start_time_value[0:4])
    s_month=int(start_time_value[8:10])
    s_day=int(start_time_value[5:7])
    s_hour=int(start_time_value[11:13])
    s_min=int(start_time_value[14:16])
    s_sec=int(start_time_value[17:19])
    tweets = getTweets(userId,start_time_value,end_time_value)
    if tweets.data == None:
        pass
        #return None
    
    else:
        while (tweets[0][-1]['created_at'] > datetime(s_year, s_month, s_day, s_hour, s_min, s_sec).replace(tzinfo=utc)):
            print(tweets[0][-1]['created_at'])
            f=tweets[0][-1]['created_at']
            end_time_value=f.strftime('%Y-%m-%d'+'T'+'%H:%M:%S'+'Z')
            tweets = getTweets(userId,start_time_value,end_time_value)
            if tweets.data == None:
                print("No hay tweets en data")
                break
          
            else:
                tweetstotal1 = getTweets_format(userId,var_username,start_time_value,end_time_value,country,election_year,results_tweets,tweets,descrip,obj)
        return tweetstotal1

def getTweets(userId,start_time_value,end_time_value):
    #results_tweets = []
    client = getClient()
    
    tweets = client.get_users_tweets(id=userId,
                                     tweet_fields = ['created_at',
                                                  'public_metrics'],
                                     start_time = start_time_value,
                                     end_time = end_time_value,
                                    max_results = 100)
    
    return tweets

def getUserId(v_username):
    
    client = getClient()
    
    userId = client.get_user(username=v_username, user_fields=['description'])
    
    if userId.data == None:
        obj = ['None','None']
    
    else :
        user_id=userId.data['id'] 
        user_description=userId.data['description']
        
        obj=[user_id,user_description]
    
    return obj

def getTweets_format(userId,var_username,start_time_value,end_time_value,country,election_year,results_tweets,tweets,descrip,obj):
    tweet_data = tweets.data
    if not tweet_data is None and len(tweet_data) > 0:
        for tweet in tweet_data:
            print(tweet.id)
            obj['country'].append(country)
            obj['election_year'].append(election_year)
            obj['username'].append(var_username)
            obj['userId'].append(userId)
            obj['userDescription'].append(descrip)
            obj['start_time'].append(start_time_value)
            obj['end_time'].append(end_time_value)
            obj['id'].append(tweet.id)
            obj['text'].append(tweet.text)
            obj['created_at'].append(tweet["created_at"])
            obj['retweet_count'].append(tweet['public_metrics']["retweet_count"])
            obj['reply_count'].append(tweet['public_metrics']["reply_count"])
            obj['like_count'].append(tweet['public_metrics']["like_count"])
            obj['quote_count'].append(tweet['public_metrics']["quote_count"])
            #results_tweets.append(obj)
        results_tweets1=pd.DataFrame.from_dict(obj)
        results_tweets = results_tweets.append(results_tweets1)
            
    else:
        obj_pd = nonTweets(var_username,country,election_year,userId,results_tweets,descrip)
        results_tweets=results_tweets.append(obj_pd)
    
    return results_tweets
    
def nonTweets(var_username,country,election_year,userId,results_tweets,descrip):
    #results_tweets = []
    names_columns=['country','election_year','username','userId','userDescription','start_time','end_time','id','text','created_at','retweet_count','reply_count','like_count','quote_count']
    obj = {k: [] for k in names_columns}
    obj['country'].append(country)
    obj['election_year'].append(election_year)
    obj['username'].append(var_username)
    obj['userId'].append(userId)
    obj['userDescription'].append(descrip)
    obj['start_time'].append('-')
    obj['end_time'].append('-')
    obj['id'].append('-')
    obj['text'].append('-')
    obj['created_at'].append('-')
    obj['retweet_count'].append('-')
    obj['reply_count'].append('-')
    obj['like_count'].append('-')
    obj['quote_count'].append('-')
    obj_pd=pd.DataFrame.from_dict(obj)
    
    return obj_pd

def get_all_tw_user1(userId,var_username,start_time_value,end_time_value,tw_election_value,dic):
    print(var_username)
    client = tf.getClient()
    utc=pytz.UTC
    s_year=int(start_time_value[0:4])
    s_month=int(start_time_value[8:10])
    s_day=int(start_time_value[5:7])
    s_hour=int(start_time_value[11:13])
    s_min=int(start_time_value[14:16])
    s_sec=int(start_time_value[17:19])
    tweets = tf.getTweets(userId,start_time_value,end_time_value)
            
    if tweets.data == None:
        pass
        #return None    
    else:
        for tweet in tweets.data:
            dic[tw_election_value]['tweets'].append(tweet.text)
            dic[tw_election_value]['created_at'].append(tweet["created_at"])
            dic[tw_election_value]['retweet_count'].append(tweet['public_metrics']["retweet_count"])
            dic[tw_election_value]['reply_count'].append(tweet['public_metrics']["reply_count"])
            dic[tw_election_value]['like_count'].append(tweet['public_metrics']["like_count"])
            dic[tw_election_value]['quote_count'].append(tweet['public_metrics']["quote_count"])
        
        while (tweets[0][-1]['created_at'] > datetime(s_year, s_month, s_day, s_hour, s_min, s_sec).replace(tzinfo=utc)):
            print(tweets[0][-1]['created_at'])
            f=tweets[0][-1]['id']
            tweets = client.get_users_tweets(id=userId,tweet_fields = ['created_at','public_metrics'],
                                             until_id=f,max_results = 100)
            if tweets.data == None:
                print("No hay tweets en data")
                break
          
            else:
                for tweet in tweets.data:
                    dic[tw_election_value]['tweets'].append(tweet.text)
                    dic[tw_election_value]['created_at'].append(tweet["created_at"])
                    dic[tw_election_value]['retweet_count'].append(tweet['public_metrics']["retweet_count"])
                    dic[tw_election_value]['reply_count'].append(tweet['public_metrics']["reply_count"])
                    dic[tw_election_value]['like_count'].append(tweet['public_metrics']["like_count"])
                    dic[tw_election_value]['quote_count'].append(tweet['public_metrics']["quote_count"])
    
    return dic
