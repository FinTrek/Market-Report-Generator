import tkinter as tk
from WindPy import *
import datetime
import time
import sys
import Services
import Index_Overview
import Derivatives_Overview
import XueQiuSpider_Find3Pages


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.StockIndexButton = tk.Button(self)
        self.StockIndexButton["text"] = "股票市场"
        self.StockIndexButton["command"] = self.StockIndex
        self.StockIndexButton.pack(side="top")

        self.VolumeButton = tk.Button(self)
        self.VolumeButton["text"] = "成交量"
        self.VolumeButton["command"] = self.Volume
        self.VolumeButton.pack(side="top")

        self.StrategyButton = tk.Button(self)
        self.StrategyButton["text"] = "宏观策略"
        self.StrategyButton["command"] = self.Strategy
        self.StrategyButton.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def StockIndex(self):
        # TODO: Make the "DATE" inputable
        DATE = '20181221'
        # Chinese Market
        Stock_ID_CN = '000001.SH,399001.SZ,399006.SZ'
        Stock_ID_List_CN = Stock_ID_CN.split(',')
        print(Index_Overview.overview_china(Stock_ID_List_CN, DATE), end='')
        # US Market
        Stock_ID_US = "DJI.GI,SPX.GI,IXIC.GI"
        Stock_ID_List_US = Stock_ID_US.split(',')
        print(Index_Overview.overview_others('美国三大股指', Stock_ID_List_US, DATE), end='')
        # European Market
        Stock_ID_US = "FTSE.GI,FCHI.GI,GDAXI.GI"
        Stock_ID_List_US = Stock_ID_US.split(',')
        print(Index_Overview.overview_others('欧洲三大股指', Stock_ID_List_US, DATE), end='')
        # Asian Market
        Stock_ID_Asia = "N225.GI,KS11.GI,AS51.GI"
        Stock_ID_List_Asia = Stock_ID_Asia.split(',')
        print(Index_Overview.overview_others('亚太股市', Stock_ID_List_Asia, DATE))

    def Volume(self):
        # TODO: Make the "DATE" inputable
        DATE = '20181221'
        Stock_ID_CN = '000001.SH,399001.SZ,399006.SZ'
        Stock_ID_List_CN = Stock_ID_CN.split(',')
        print(Index_Overview.volume(Stock_ID_List_CN, DATE))

    def Strategy(self):
        DATE = '20181221'
        print(XueQiuSpider_Find3Pages.get_comment(date=DATE), end='\n')


if __name__ == "__main__":
    w.start()
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()