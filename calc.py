import pandas as pd
import numpy as np
import datetime as dt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

data = pd.read_csv("data1.csv")

#calculating MSD value for userdefined window
def MSD(data, n):
    data["close_std"] = data["Close"].rolling(n).std()
    data["atr_std"] = data["atr"].rolling(n).std()
    return data

def plots(data):

     #candle stick graph for bonds future
    Candle = go.Candlestick(
        x=data["Date"],
        open=data["Open"],
        high=data["High"],
        low=data["Low"],
        close=data["Close"],
        legendgroup="Price",
        name="Price",
    )
    #Average True Range Graph
    ATR = go.Scatter(
        x=data["Date"], y=data["atr"], legendgroup="ATR", name="Average True Range"
    )
    #Moving Standard Deviation graph
    ATR_STD = go.Scatter(
        x=data["Date"], y=data["atr_std"], legendgroup="ATR_STD", name="ATR MSD"
    )
    ATR_CLOSE = go.Scatter(
        x=data["Date"],
        y=data["close_std"],
        legendgroup="CLOSE_STD",
        name="CLOSE Price MSD",
    )

    fig = make_subplots(
        rows=5,
        cols=1,
        shared_xaxes=True,
        shared_yaxes=False,
        vertical_spacing=0.075,
        row_width=[3, 3, 3, 0.1, 10],
        subplot_titles=(
            "Bond Price Over the time",
            "",
            "Average True Range",
            "ATR Moving Standard Deviation",
            "CLOSE Price Moving Standard Deviation",
        ),
    )
    fig.append_trace(Candle, row=1, col=1)

    fig.append_trace(ATR, row=3, col=1)

    fig.append_trace(ATR_STD, row=4, col=1)

    fig.append_trace(ATR_CLOSE, row=5, col=1)

    fig.update_layout(
        title_text="German 10 YR Bund Futures - Jun 22"
    )

    #adding time frame buttons
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=[
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all"),
                ]
            ),
            type="date",
            rangeslider_thickness=0.05,
        )
    )
    fig.update_layout(showlegend=False)
    #axis lines
    fig.update_xaxes(showline=True, linewidth=2, linecolor="black", mirror=True)
    fig.update_yaxes(showline=True, linewidth=2, linecolor="black", mirror=True)
    fig.update_xaxes(showgrid=True)
    fig.update_yaxes(showgrid=True)
    return fig


def execute(data, n):
    data = MSD(data, n)
    fig = plots(data)
    close = data["Close"].iloc[-1]
    change = float(data["Change %"].iloc[-1][:-1])
    date = data["Date"].iloc[-1]
    return fig, close, change, date
