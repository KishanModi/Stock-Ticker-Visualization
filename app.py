import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
import time
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
pio.templates.default = "plotly_white"
data = pd.read_csv('final.csv')


st.set_page_config(layout="wide")

## Main Title ##
st.title('Data Visualization')

Candle = go.Candlestick(x=data['Date'],
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'],legendgroup="Price",name="Price")
ATR = go.Scatter(x=data['Date'],
                y=data['atr'],legendgroup="ATR",name="ATR")

ATR_STD = go.Scatter(x=data['Date'],
                y=data['atr_std'],legendgroup="ATR_STD",name="ATR_STD")
ATR_CLOSE = go.Scatter(x=data['Date'],
                y=data['close_std'],legendgroup="CLOSE_STD",name="CLOSE_STD")

fig = make_subplots(rows=5, cols=1,
                          shared_xaxes=True, shared_yaxes=False,
                           vertical_spacing=0.075,row_width=[3,3,3,0.1,10],subplot_titles=("Price", "","ATR", "ATR_STD", "CLOSE_STD"))
fig.append_trace(Candle, row=1, col=1)

fig.append_trace(ATR,row=3, col=1)

fig.append_trace(ATR_STD,row=4, col=1)

fig.append_trace(ATR_CLOSE,row=5, col=1)


fig.update_layout(title_text="Data Visualization",
                  height=900, width=1400)
# fig.update_xaxes(
#     rangeselector=dict(
#         buttons=list([
#             dict(count=1, label="1m", step="month", stepmode="backward"),
#             dict(count=6, label="6m", step="month", stepmode="backward"),
#             dict(count=1, label="YTD", step="year", stepmode="todate"),
#             dict(count=1, label="1y", step="year", stepmode="backward"),
#             dict(step="all")
#         ])
#     ),
#     xaxis2_rangeslider_visible=True,
#     xaxis2_type="date"
# )
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=[
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ]),
        type="date",rangeslider_thickness = 0.05)
    )

with st.container():
	st.plotly_chart(fig,use_container_width=True)