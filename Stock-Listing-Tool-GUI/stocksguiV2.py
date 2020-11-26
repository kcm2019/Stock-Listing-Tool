import tkinter as tk
from tkinter import filedialog, Text
import os

class StocksGUI:
    def __init__(self):
        root = tk.Tk()
        stocks =[]

        canvas = tk.Canvas(root, height=600, width=600, bg="#263D42")
        canvas.pack()

        frame = tk.Frame(root, bg="white")
        frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        addStock = tk.Button(root,text="Add Stock", padx=10, pady=5, fg="white", bg="#263D4")
        addStock.pack()

        root.mainloop()        

    def getStockInfo(str):
        try:
            print(str)
            string = str.rstrip()
            page = requests.get("https://finance.yahoo.com/quote/" + string +"/")
            soup = BeautifulSoup(page.content, 'html5lib') #lxml

            price = soup.find(class_ = "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
            percent = soup.find(class_ =  "Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)")
            if (percent == None):
                percent = soup.find(class_ =  "Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)")
            print(price.get_text())
            print(percent.get_text())
        except:
            print("Error")

    def addStock():
        for widget in frame.winfo_children():
            widget.destroy()
            
    
