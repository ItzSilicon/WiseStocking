import requests
from bs4 import BeautifulSoup
import twstock
import random
import yfinance as yf
import json
import glob
import os


def loadConfig():
    fd = open("Config.json", 'r', encoding="utf-8")
    d = fd.read()
    Set = json.loads(d)
    fd.close()
    return Set


def GetWebContent(URL):  # get html content
    Content = requests.get(URL)
    return Content.text


def Getstockwebinfo(code):  # get stock info on tw.stock.yahoo
    stockweb = GetWebContent(f'https://tw.stock.yahoo.com/quote/{code}')
    return stockweb


def Htmlize(web):  # Turn content into html format
    return BeautifulSoup(web, 'html.parser')


def GetElm(web, Elm):  # find element from html
    return Htmlize(web).find(Elm)


def GetRealtimePrice(id):  # get realtime info by entering stock code
    return twstock.realtime.get(id)


def randstock():  # generate random stock code
    code = random.randint(1011, 9999)
    code = str(code)
    return code


def getstockinfo(code):
    stock = yf.Ticker(code)
    info = stock.info
    return (info)


def update(code):
    try:
        D = getstockinfo(f"{code}.tw")
    except:
        return None
    S = json.dumps(D)
    with open(f"StockLibrary/{code}.json", "w") as f:
        f.write(S)
        print(f"{code}.json Updated.")


def importinfo():
    N = {}
    L = glob.glob(os.path.join("StockLibrary", "*"))
    for i in L:
        code = i[13:17]
        update(code)
        try:
            with open(i, 'r', encoding='utf-8') as f:
                S = f.read()
                # print(S)
                C = json.loads(S)
                D = C["longName"]
                # print(type(D))
                N[i] = D
                G = json.dumps(N)
                with open("StockLibrary/Name.json", "w") as k:
                    k.write(G)
        except KeyError:
            continue
