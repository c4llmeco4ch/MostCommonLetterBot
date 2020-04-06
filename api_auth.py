import tweepy
import os

def init_API_object():
    """create a tweepy object that is authenticated"""
    auth = tweepy.OAuthHandler(os.environ.get('TW_API'),
                                os.environ.get('TW_API_SEC'))
    auth.set_access_token(os.environ.get('TW_ACC'),
                          os.environ.get('TW_ACC_SEC'))
    api=tweepy.API(auth)
    return api