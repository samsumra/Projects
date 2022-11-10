import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
## Sam's Stock App

Shown are the stock **closing price** and **volume** of:
1. Vanguard Total Stock Market ETF (VTI)
2. Vanguard S&P 500 ETF (V00)

""")

# https://towardatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# define the ticker symbol
tickerSymbol = 'VTI'
tickerSymbol2 = 'VOO'
# get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
tickerData2 = yf.Ticker(tickerSymbol2)
# get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2015-11-07', end='2022-11-07')
tickerDf2 = tickerData2.history(period='1d', start='2015-11-07', end='2022-11-07')
# Open High     Low close       Volume Dividends        Stock Splits

st.write("""
### Closing Price
VTI
""")
st.line_chart(tickerDf.Close)
st.write("VOO")
st.line_chart(tickerDf2.Close)

st.write("""
### Volume Price
VTI
""")
st.line_chart(tickerDf.Volume)
st.write("VOO")
st.line_chart(tickerDf2.Volume)

st.write("""##### Learn More
[VTI v VOO](https://finance.yahoo.com/news/vti-vs-voo-etf-best-135350433.html#:~:text=The%20most%20notable%20difference%20between,of%20the%20S%26P%20500%20Index.)
""")
