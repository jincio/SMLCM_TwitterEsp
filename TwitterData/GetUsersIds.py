#Packages
from passwords import *
import numpy as np
import tweepy
import json
import pandas as pd
import time

### Output a data frame with USERS' Ids. 

### Functions 
def getClient():
    client=tweepy.Client(bearer_token=bearer_token,
                         consumer_key=consumer_key,
                         consumer_secret=consumer_secret,
                         access_token=access_token,
                         access_token_secret=access_token_secret,
                         wait_on_rate_limit=True)
    
    return client

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

#### Data mungin

data=pd.read_excel('../DisData/Raw/datacandidatos.xlsx', sheet_name='datacandidatos')
data['Twitterhandle']=data['Twitterhandle'].str.replace("@","")#
data['Twitterhandle']=data['Twitterhandle'].str.replace(" ","")#
###
s1=data['Twitterhandle'].unique()
s1 ### array of Twitterhandles

#### New Data Frame

usersDf=pd.DataFrame()
usersDf['Twitterhandle']=s1
len(usersDf)

#### Getting Twitter UserIDs and Description

for i in range(0,len(usersDf)):
    index=i
    print(usersDf['Twitterhandle'][i])
    DeId=getUserId(usersDf['Twitterhandle'][i])
    usersDf.loc[index,'userId'] =str(DeId[0])
    usersDf.loc[index,'description'] =str(DeId[1])

### Saving DataFrame.
usersDf.to_excel('Twitter_OutputData/TUsersIdsPresidential.xlsx')
