import streamlit as st

st.title('Test')

passcode = st.text_input('passcode', type='password')
sumbitted = st.button('Sumbit')

if sumbitted and passcode ==  st.secrets['passcode']:
    st.write('pass')
else:
    st.write('No!')
