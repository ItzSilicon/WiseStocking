import yfinance as yf

# 获取股票数据
ticker = "2330.tw"  # 股票代码，例如苹果公司的代码是 AAPL
stock = yf.Ticker(ticker)

# 获取财务报表数据
print(stock.balancesheet)
