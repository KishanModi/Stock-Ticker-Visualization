import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
import time
import plotly.graph_objects as go
from plotly.subplots import make_subplots


data = pd.read_csv('final.csv')


st.set_page_config(layout="wide")

## Main Title ##
st.title('Data Visualization')

Candle = go.Candlestick(x=data['Date'],
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'])
ATR = go.Scatter(x=data['Date'],
                y=data['atr'])

ATR_STD = go.Scatter(x=data['Date'],
                y=data['atr_std'])
ATR_CLOSE = go.Scatter(x=data['Date'],
                y=data['close_std'])

fig = make_subplots(rows=4, cols=1,
                          shared_xaxes=True, shared_yaxes=False,
                          vertical_spacing=0.1,row_width=[3,3,0.5,14])
fig.append_trace(Candle, row=1, col=1)

fig.append_trace(ATR,row=3, col=1)

fig.append_trace(ATR_STD,row=4, col=1)

fig.append_trace(ATR_CLOSE,row=4, col=1)


fig.update_layout(height=700, width=1000,
                  title='Data Visulization',
                  title_text="Multiple Subplots with Titles")
fig.layout.yaxis2.showgrid=False
with st.container():
	st.plotly_chart(fig,use_container_width=True)