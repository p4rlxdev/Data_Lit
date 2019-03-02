import tweepy
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# twitter API authentication variables
consumer_key = 'L7C5SK4ORhYoLS31Hgm7ibBfk'
consumer_secret = 'GtMikw9q8VbcdPTJXGuf395jSN2GRos0sLhOnWfOTDqrrIl3xv'
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = api.search('Chelsea', count=200)

data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])

print(data.head(10))

print(tweets[0].created_at)

# import nltk
# nltk.download('vader_lexicon')

sid = SentimentIntensityAnalyzer()

listy = []

for index, row in data.iterrows():
    ss = sid.polarity_scores(row["Tweets"])
    listy.append(ss)

se = pd.Series(listy)
data['polarity'] = se.values

print(data.head(20))
