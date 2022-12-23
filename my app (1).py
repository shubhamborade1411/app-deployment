#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit as st
import yfinance as yf
st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Google!
""")

 
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open High Low Close Volume Dividends Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)


# In[ ]:




