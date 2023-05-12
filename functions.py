from time import ctime
class log:
    
    def __init__(self):
        self.time = ctime()
        self.fd = open("log.log", "a", encoding="utf-8")
        
    def print(self, msg):
        print(msg)
        self.fd.write(f"[{self.time}] [PRINT] {msg}\n")
        
    def error(self, msg):
        self.print("Something went wrong,please check the log file.")
        self.fd.write(f"[{self.time}] [ERROR] {msg}\n")
        
    def info(self, msg):
        self.fd.write(f"[{self.time}] [INFO] {msg}\n")
        
    def debug(self, msg):
        self.fd.write(f"[{self.time}] [DEBUG] {msg}\n")
        
    def input(self, msg):
        self.fd.write(f"[{self.time}] [INPUT] {msg}\n")
        enter=input(msg)
        self.debug(f"The input is: {enter}")
        return enter
        
    def warning(self, msg):
        self.fd.write(f"[{self.time}] [WARNING] {msg}\n")
        
    def __del__(self):
        self.fd.close()

global logger
logger=log()
logger.info("Importing functions...")
try:
    import requests
    from bs4 import BeautifulSoup
    import twstock
    import random
    import yfinance as yf
    import json
    import glob
    import os
    logger.info("""The following modules are loaded successfully:requests,bs4,twstock,yfinance,json,glob,os""")
except Exception as msg:
    logger.error(msg)
    exit(1)





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
    logger.info(f"Getting {URL}...")
    try:
        Content = requests.get(URL)
        return Content.text
    except Exception as msg:
            logger.error(msg)
    


def get_stockweb_info(code):  # get stock info on tw.stock.yahoo
    """
    擷取tw.stock.yahoo資料
    Args:
        code (str): 輸入股票代碼，作為網址的一部份

    Returns:
        str: 回傳該頁面資料
    """
    logger.info(f"Getting stock info on tw.stock.yahoo...")
    try:
        stockweb = get_web_content(f'https://tw.stock.yahoo.com/quote/{code}')
        return stockweb
    except Exception as msg:
        logger.error(msg)
        return None


def htmlize(web):  # Turn content into html format
    """
    格式化HTML

    Args:
        web (str): 網頁原始碼

    Returns:
        str: 格式化後的網頁原始碼
    """
    try:
        logger.info(f"Converting {web} to html format...")
        soup = BeautifulSoup(web, 'html.parser')
        return soup
    except Exception as msg:
        logger.error(msg)
        return None


def get_elm(web, elm):  # find element from html
    """
    查找指定元素

    Args:
        web (str): 網頁原始碼
        elm (str): 指定的元素

    Returns:
        str: 指定的元素
    """
    try:
        logger.info(f"Finding {elm}...")
        htmlize(web)
        return htmlize(web).find(elm).get_text()
    except Exception as msg:
        logger.error(msg)
        return None     


def get_realtime_price(id): 
    logger.info(f"Getting realtime info by entering stock code {id}...")
    
    temp=twstock.realtime.get(id)
    logger.info(f"Getting realtime info by entering stock code {id} successfully.")
    return temp


def randstock():  # generate random stock code
    """"""
    code = random.randint(1011, 9999)
    code = str(code)
    logger.info(f"Generating random stock code {code}")
    return code


def getstockinfo(code):
    logger.info(f"Getting stock info by entering stock code {code}...")
    stock = yf.Ticker(code)
    info = stock.info
    return (info)


def update(code:str):
    logger.info(f"Updating Stock Library...")
    try:
        data = getstockinfo(f"{code}.tw")
    except requests.exceptions.HTTPError as e:
        logger.error(e)
        print(e)
        return None
    logger.info(f"Updating Stock Library successfully.")
    S = json.dumps(data)
    with open(f"StockLibrary/{code}.json", "w",encoding="utf-8") as fd:
        fd.write(S)
        print(f"{code}.json Updated.")


def importinfo():
    """AI is creating summary for importinfo
    """
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

logger.info("Import functions successfully.")