__author__ = 'eribeiro'

import urllib.request
import re


def html_from_url(url):
    page = urllib.request.urlopen(url)
    return str(page.read())


def problem8():
    url = "https://projecteuler.net/problem=8"
    html = html_from_url(url)
    nums = re.findall('\d{50}', html)
    return "".join(nums)
