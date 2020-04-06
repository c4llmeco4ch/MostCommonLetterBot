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
            query += convert_datestr_to_query(val)
    return query


def convert_datestr_to_query(datestr: str) -> str:
    """
    Provided a date in d:m:y format,
    return a string in 'since:yyyy-mm-dd' format
    """
    try:
        parsed = parseDate(datestr)
    except ValueError:
        return False
    return 'since%3A{year}%2D{month}%2D{day}'.format(
            year=parsed.year, month=parsed.month, day=parsed.day
            )


def parseDate(d: str) -> date:
    """
    Provided a date in d:m:y format,
    return a corresponding date object
    """
    vals = [int(val) for val in d.split(':')]
    return date(vals[2], vals[0], vals[1])
