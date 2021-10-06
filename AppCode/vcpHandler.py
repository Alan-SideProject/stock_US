#---------------------------------------
# [File]: vcpHandler.py
#---------------------------------------
# import yfinance as yf
# from finviz.screener import Screener
# import pandas as pd
# import numpy as np
# from tqdm import tqdm
# from scipy.stats import linregress
# from IPython.core.display import HTML
from finvizfinance.quote import finvizfinance
from IPython.display import Image ,display

# class Vcp:
#     def __init__(self,ticket):# Constructor
#         self.ticket = ticket

def ShowImageTest(ticker):
    stock = finvizfinance(ticker)
    print(stock.TickerCharts(out_dir='image'))
    display(Image(url= stock.TickerCharts(out_dir='image')))