from bs4 import BeautifulSoup
import requests

def getStockInfo(str):
    try:
        print(str)
        string = str.rstrip()
        page = requests.get("https://finance.yahoo.com/quote/" + string +"/")
        soup = BeautifulSoup(page.content, 'lxml')

        price = soup.find(class_ = "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
        percent = soup.find(class_ =  "Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)")
        if (percent == None):
            percent = soup.find(class_ =  "Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)")
        print(price.get_text())
        print(percent.get_text())
    except:
        print("Error")


stockList = open("stocklist.txt", "r")
stocksStr = stockList.readlines()
count = len(stocksStr)
print(stocksStr)
print(count)

for k in range (0, count):
    getStockInfo(stocksStr[k])

#stock1 = input("Stock 1: ")
#getStockInfo(stock1)

#stock2 = input("Stock 2: ")
#getStockInfo(stock2)
