from functions import log
global logger
logger=log()
try:
    import functions
    import sys
    import os  #Use of Windows Prompt
except Exception as msg:
    logger.error(msg)
    sys.exit(1)



def load_config():
    try:
        setting=functions.load_data_config()
    except Exception as msg:
        logger.error(msg)
        sys.exit(1)
    return setting
    




def getinfo(code):  #Get Stock info
  try:
    info = functions.get_realtime_price(code)
    return (info)
  except Exception as msg:
      logger.error(msg)
      sys.exit(1)


def rand():  #Generate random stock code and get its info
  global info
  code = functions.randstock()  #random generate a code with 4 digits.
  # print(code,end=' ')
  info = getinfo(code)
  if not info['success']:
    logger.debug("Stock code is not exist.")
    # print('not exist.')
    rand()  #Recursion
  else:
    logger.debug("Stock code is exist.")
    # print('exist.')


def clear():  #clear cmd
  os.system('clear')



cmd = logger.input(
  "Enter stock code or a command with '/':\n")  #Input command or code\
if cmd == '/randstock':
  logger.print('Generating random stock code...')
  rand()
  stockdata = info

else:
  logger.print('Getting stock infomation...')
  stockdata = getinfo(cmd)

# print(stockdata)
logger.print('Arranging stock infomation...')

try:
  class Stockinfo:  #define the stock info founded.
    code = stockdata['info']['code']
    name = stockdata['info']['name']
    fullname = stockdata['info']['fullname']
    endtime = stockdata['info']['time']
    price = eval(stockdata['realtime']['latest_trade_price'])
    vol = eval(stockdata['realtime']['trade_volume'])
    accvol = eval(stockdata['realtime']['accumulate_trade_volume'])
    openprice = eval(stockdata['realtime']['open'])
    highest = eval(stockdata['realtime']['high'])
    lowest = eval(stockdata['realtime']['low'])
except KeyError:
  logger.error(f"The stock code {cmd} is not exist.")
  sys.exit(1)


detail = f"""
Code: {Stockinfo.code}
Cooperation/Stock Name: {Stockinfo.name} ({Stockinfo.fullname})
Closing time: {Stockinfo.endtime}
Price(per stock): {Stockinfo.price}
Volume: {Stockinfo.vol}
Accumulate Volume: {Stockinfo.accvol}
Opening Price: {Stockinfo.openprice}
Highest: {Stockinfo.highest}
Lowest: {Stockinfo.lowest}
"""

logger.print(detail)