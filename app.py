import numpy as np
import pandas as pd
import yfinance as yf
import streamlit as st
import auth

st.title('Test')

# passcode = st.text_input('passcode', type='password')
# sumbitted = st.button('Sumbit')

# passcode ==  st.secrets['passcode']:

conn = auth.Connect()
db = conn.get_collection('holdings')

# docs = db.get()

# for doc in docs:
#     st.write(f"{doc.id} => {doc.to_dict()}")

# st.write([
#     doc.id for doc in docs
# ])

# holdings = list(conn.get_collection('holdings').stream())

# users_dict = list(map(lambda x: x.to_dict(), holdings))
# df = pd.DataFrame(users_dict)

docs = db.stream()

items = list(map(lambda x: {'ticker': x.id, **x.to_dict()}, docs))

df = pd.DataFrame(items) # , columns=['id', 'email']
#df.set_index('id', inplace=True)

prices = []
for ticker in df['ticker']:
    prices.append(yf.Ticker(ticker).info['previousClose'])

df['price'] = prices
df['value'] = df.price * df.quantity

st.metric('NAV', df.value.sum())

st.dataframe(df) #hide_index=None