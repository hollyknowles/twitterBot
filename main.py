from bs4 import BeautifulSoup
from datetime import datetime
from dateutil.relativedelta import relativedelta, MO
import requests
import re


def get_date_ten_years_ago():
    """This function returns the date 10 years ago"""
    return datetime.now() - relativedelta(years=10)


def make_day_monday(date):
    """The NZ Top 40 updates every Monday so will need to change date 10 years to be the Monday thats just passed"""
    if date.weekday() == 0:
        return date
    else:
        return date + relativedelta(weekday=MO(-1))


def string_extract(string):
    start = '<h3 class="artist"><span>'
    end = '</span></h3>'
    temp = string[string.find(start) + len(start):string.rfind(end)]
    escaped_string = re.escape(temp)
    return escaped_string


def get_top_single_nz_top_40():
    """This function gets the #1 single from the NZ Top 40 charts on this day 10 years ago
        https://nztop40.co.nz/chart/singles
    """
    url = "https://nztop40.co.nz/chart/singles"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # by default soup.find gets the first match it can find - which is what I want
    top_song = soup.find("h2", {"class": "title"})
    top_artist = re.escape(soup.find("h3", {"class": "artist"}))
    # print(top_artist)
    # x = string_extract(top_artist)
    print(top_artist)


# print(make_day_monday(get_top_single_nz_top_40()))
get_top_single_nz_top_40()
# start = '<h3 class="artist"><span>'
# end = '</span></h3>'
# print(start)
# print(end)
# x = "<h3 class="artist"><span>Jack Harlow</span></h3>"
# string_extract(x)
