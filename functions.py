import requests
from bs4 import BeautifulSoup
import twstock
import random
import yfinance as yf
import json
import glob
import os
from time import ctime


class log:
    def __init__(self):
        self.time = ctime()
        self.fd = open("log.txt", "a", encoding="utf-8")
        
    def write(self, msg):
        print(msg)
        self.fd.write(f"[PRINT] [{self.time}] {msg}\n")
        
    def error(self, msg):
        self.write("Something went wrong,please check the log file.")
        self.fd.write(f"[ERROR] [{self.time}] {msg}\n")
        
    def info(self, msg):
        self.fd.write(f"[INFO] [{self.time}] {msg}\n")
        
    def debug(self, msg):
        self.fd.write(f"[DEBUG] [{self.time}] {msg}\n")
        
    def warning(self, msg):
        self.fd.write(f"[WARNING] [{self.time}] {msg}\n")
        
    def __del__(self):
        self.fd.close()

global logger
logger=log()
def load_data_config():
    logger=log()
    """載入初值設定

    Returns:
        dict: 初值設定，以字典形式儲存
    """
    logger.info("Loading Config.json...")
    fd = open("Config.json", 'r', encoding="utf-8")
    data = fd.read()
    setting = json.loads(data)
    fd.close()
    logger.info("Config.json loaded successfully.")    
    return setting


def get_web_content(URL):
    """
    擷取網頁資料
    Args:
        URL (str): 輸入網址

    Returns:
        Response: 回傳網頁資料
    """
    Content = requests.get(URL)
    return Content.text


def get_stockweb_info(code):  # get stock info on tw.stock.yahoo
    """
    擷取tw.stock.yahoo資料
    Args:
        code (str): 輸入股票代碼，作為網址的一部份

    Returns:
        str: 回傳該頁面資料
    """
    stockweb = get_web_content(f'https://tw.stock.yahoo.com/quote/{code}')
    return stockweb


def htmlize(web):  # Turn content into html format
    """
    格式化HTML

    Args:
        web (str): 網頁原始碼

    Returns:
        str: 格式化後的網頁原始碼
    """
    return BeautifulSoup(web, 'html.parser')


def get_elm(web, elm):  # find element from html
    return htmlize(web).find(elm)


def get_realtime_price(id):  # get realtime info by entering stock code
    return twstock.realtime.get(id)


def randstock():  # generate random stock code
    code = random.randint(1011, 9999)
    code = str(code)
    return code


def getstockinfo(code):
    stock = yf.Ticker(code)
    info = stock.info
    return (info)


def update(code:str):
    try:
        data = getstockinfo(f"{code}.tw")
    except requests.exceptions.HTTPError as e:
        print(e)
        return None
    S = json.dumps(data)
    with open(f"StockLibrary/{code}.json", "w",encoding="utf-8") as fd:
        fd.write(S)
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

