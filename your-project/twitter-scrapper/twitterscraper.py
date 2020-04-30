from twitterscraper import query_tweets
import datetime as dt
import pandas as pd
import time

day_delta = dt.timedelta(days=1)
start_date = dt.date(2020, 1, 1)
final_date = dt.date(2020, 1, 2) ##dummy date to avoid running whole code
while start_date > final_date:
    begin_date = start_date - 7*day_delta
    end_date = start_date
    
    query = '"Barcelona" AND "violencia" OR "crimen" OR "inseguridad" OR "delincuencia" OR "agresion" OR "delito" OR "crim" OR "inseguretat" OR "delinqüència" OR "agressió" OR "delicte"'
    tweets = query_tweets(query=query, begindate = begin_date, enddate = end_date)
    
    print(len(tweets), f' were retrieved for {begin_date} to {end_date}')
    print(tweets)
