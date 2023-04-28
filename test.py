import Functions as Fx  #Import functions from Fuctions.py and define it Fx.
import os  #Use of Windows Prompt



def getinfo(code):  #Get Stock info
  info = Fx.GetRealtimePrice(code)
  return (info)


def rand():  #Generate random stock code and get its info
  global info
  code = Fx.randstock()  #random generate a code with 4 digits.
  # print(code,end=' ')
  info = getinfo(code)
  if not info['success']:  #Invalid Stock Code
    # print('not exist.')
    rand()  #Recursion


def clear():  #clear cmd
  os.system('clear')



cmd = input(
  "Enter stock code or a command with '/':\n")  #Input command or code\

if cmd == '/randstock':
  print('Searching...')
  rand()
  stockdata = info

else:
  print('Getting stock infomation...')
  stockdata = getinfo(cmd)

# print(stockdata)
print('Arranging stock infomation...')


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

print(detail)
