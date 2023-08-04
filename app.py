import numpy as np
import pandas as pd
import streamlit as st
import auth

st.title('Test')

# passcode = st.text_input('passcode', type='password')
# sumbitted = st.button('Sumbit')

# passcode ==  st.secrets['passcode']:

conn = auth.Connect()
db = conn.get_collection('holdings')

docs = db.get()

for doc in docs:
    st.write(f"{doc.id} => {doc.to_dict()}")

st.write([
    doc.id for doc in docs
])


db = firestore.Client()
holdings = list(conn.get_collection('holdings').stream())

users_dict = list(map(lambda x: x.to_dict(), holdings))
df = pd.DataFrame(users_dict)
st.dataframe(df)