import requests
import datetime
import typing
import json
from typing import List
from requests import Response

def obtain_dailies(day: date = datetime.today(), lang: str = 'en') -> Response:
    """Given a date and language, pull all tweets from with those specifications"""
    pass

def build_API_request(**kwargs: str) -> str:
    """Construct a Twitter API request involving any number of arguments"""
    pass