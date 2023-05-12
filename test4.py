import functions 

code="2330"
url=f"https://mops.twse.com.tw/server-java/t164sb01?step=1&CO_ID={code}&SYEAR=2022&SSEASON=4&REPORT_ID=C"
h=functions.get_web_content(url)
h=functions.htmlize(h)
h=h.prettify()
total_assets=h.find("<ix:nonfraction contextref="AsOf20221231" decimals="-3" format="ixt:numdotdecimal" name="ifrs-full:Assets" scale="3" unitref="TWD">")
with open("stock.html","w",encoding="utf-8") as f:
    f.write(h)
