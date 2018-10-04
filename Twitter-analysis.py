from textblob import TextBlob
import tweepy

##wiki = TextBlob("Shubham is angry as he is cheated every time")
##print(wiki.tags) #assigns tags NNP etc to the words
##wiki.words #performs word tokenization
##wiki.sentiment.polarity #tells the sentence polarity -1<polarity<1

ckey="4VAiBAB6w1zkRmZOv491JpOhv"
csecret="24J1JrSoXLQj0j468IPAuKKseentO94evrCtmqlHGVxc1CDIJZ"
atoken="1027182879401435137-2IyYON2AtzdplfPmZ3QdG8l5lqRojY"
asecret="dlwhNXVnACOs4oRyeOlcs9ERRE2cKBCekLVUmKYLtkxHS"

auth = tweepy.OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

api = tweepy.API(auth)

tweets = api.search('Modi')

for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

