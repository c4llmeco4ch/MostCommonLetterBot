import requests
from datetime import date
import typing
import json
from typing import List, Union
from requests import Response


def obtain_dailies(day: date = date.today(), lang: str = 'en') -> Response:
    """
    Given a date and language,
    pull all tweets from with those specifications
    """
    pass


def build_API_request(**kwargs: str) -> str:
    """Construct a Twitter API request involving any number of arguments"""
    pass

def build_API_query(**kwargs: str) -> Union[str, bool]:
    """
    From a list of arguments,
    create the query portion of a twitter call
    """
    if len(kwargs) == 0:
        return ''
    query = 'q='
    for key, val in kwargs.items():
        if key == 'date':
            try:
                day = parseDate(val)
            except ValueError:
                return False
            query += 'since%3A{year}%2D{month}%2D{day}'.format(
                year=day.year, month=day.month, day=day.day
            )
    return query

def parseDate(d: str) -> date:
    """
    Provided a date in d:m:y format,
    return a tuple in (y, m, d) format
    """
    vals = [int(val) for val in d.split(':')]
    print(vals)
    return date(vals[2], vals[0], vals[1])
        
    
