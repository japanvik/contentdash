# coding: utf-8
import requests
import re
from bs4 import BeautifulSoup

#Grab the top 10 Yahoo Japan Burst Ranking

def get_burst():
    url = "http://searchranking.yahoo.co.jp/rt_burst_ranking/"
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "lxml")
    ul = soup.find_all("ul", class_=re.compile("pat."))[0]
    bursts = [x.text for x in ul.select("li a")]
    return bursts


if __name__ == '__main__':
    for b in get_burst():
        print b
