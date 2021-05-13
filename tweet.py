# https://github.com/JamieLoughnane/python-tweet
import sys
try:
    import tweepy
except ModuleNotFoundError:
    sys.exit("Tweepy not found! Please enter 'pip install tweepy' into your Command Prompt/Terminal, for help using pip visit: https://pip.pypa.io/en/stable/")

print("First create a Twitter app at https://developer.twitter.com/ and then come back here to enter your keys found on the 'Keys and tokens' page of your app")

consumer_key = input("Consumer Key: ")
consumer_secret = input("Consumer Secret: ")
access_token = input("Access Token: ")
access_token_secret = input("Access Token Secret: ")
tweet = input("Enter your tweet: ")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

try:
    api.update_status(status=tweet)
except tweepy.error.TweepError as e:
    error = e.api_code
    if error == 89:
        print("Tweet failed: Authentication error")
    elif error == 170:
        print("Tweet failed: No tweet entered")
    elif error == 187:
        print("Tweet failed: Duplicate tweet")
    elif error == 186:
        print(f"Tweet failed: Too many characters (the limit is 280 characters and you entered {len(tweet)} characters)")
    else:
        print("Tweet failed: Unknown error")
    sys.exit()

print("Tweet sent!")