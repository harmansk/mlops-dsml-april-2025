import streamlit as st
import pandas as pd
import numpy as np

import yfinance as yf

# Title for our web app
st.title('Stock Market Analysis!!')

# Note: We can run this streamlit code with just title using this command in command line --> streamlit run streamlit_code_1.py
# As soon as you run the script using "streamlit run", a local Streamlit server will spin up and your app will open in a new tab in your default web browser.

# For header and subheader 
st.header('Stock Price Analysis')
st.subheader('Stock Price Data')

# To display a simple text
st.write('This is a simple stock price analysis app using Streamlit and yfinance library.')

# Different example of widgets 
if st.checkbox('Click me if you want more information'):
    st.write('This is a checkbox')
    st.write('This is a radio button')
    st.write('This is a select box')
    st.write('This is a multiselect box')
    st.write('This is a slider')
    st.write('This is a text input')
    st.write('This is a number input')
    st.write('This is a date input')
    st.write('This is a time input')
    st.write('This is a file uploader')

# -----------------------------x-------------------X-----------
# Main code of stock anlaysis starts here (above just note)	
# To get start date and end date as input from user
start_date = st.date_input('Start date', pd.to_datetime('2020-01-01'))
end_date = st.date_input('End date', pd.to_datetime('2023-01-01'))


#symbol = 'AAPL'  # Applie Inc stock . ticker_symbol to get input for any stock name.
ticker_symbol = st.text_input('Enter the stock ticker symbol', 'AAPL')


# Getting Applie stock price from yfinance lib
ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period = '1d', start=start_date, end=end_date)

# Check if the DataFrame is empty
if ticker_df.empty:
    st.error("No data found for the given ticker symbol. Please try another symbol.")
else:
    # Display the DataFrame and charts .The DF shown is interactive.
    st.dataframe(ticker_df)
    
    # Let's create some charts
    st.write('## Closing Price Chart')
    st.line_chart(ticker_df['Close'])  # inside line_chart pass the series 


    col1, col2 = st.columns(2)

    with col1:
        st.write(
            """
            ## Daily Closing Price Chart
            """
        )
        st.line_chart(ticker_df.Close)

    with col2:
        st.write(
            """
            ## Daily Volume Price Chart
            """
        )
        st.line_chart(ticker_df.Volume)

# We can also then deploy it using streamlit cloud or any other cloud service.
# To deploy it using streamlit cloud, we need to create a requirements.txt file using : pip freeze > requirements.txt 
# and then push the code to a git repository. Then we can connect the git repository to streamlit cloud and deploy it.

