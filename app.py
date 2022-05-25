import streamlit as st
import time
st.set_page_config(layout="wide")
from calc import *

data = pd.read_csv('final.csv')


st.title('German 10 YR Bund Futures - Jun 22')

#slider for MSD window
st.subheader('Enter The Moving Standard Deviation Window:')
MSDwindow = st.slider('Range', 2, 30, 14)


#submit button
if st.button('Visulize'):
    with st.spinner('Wait for it...'):
        time.sleep(1)
        fig,close,change, date = execute(data, MSDwindow)

    col1, col2 = st.columns(2)
    col1.metric("Current Price",close, change)
    col2.metric("Date", date)

    with st.container():
	    st.plotly_chart(fig,use_container_width=True)
