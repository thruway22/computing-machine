import streamlit as st
from auth import db

st.title('Test')

# passcode = st.text_input('passcode', type='password')
# sumbitted = st.button('Sumbit')

# passcode ==  st.secrets['passcode']:

# # Authenticate to Firestore with the JSON account key.
# db = firestore.Client.from_service_account_json("firestore-key.json")

# key_dict = json.loads(st.secrets["textkey"])
# creds = service_account.Credentials.from_service_account_info(key_dict)
# db = firestore.Client(credentials=creds, project="my-family-fund")

# db = Database()

# Create a reference to the Google post.
# doc_ref = db.collection("holdings").document("1120.SR")

# Then get the data at that reference.
# doc = doc_ref.get()

# # Let's see what we got!
# st.write("The id is: ", doc.id)
# st.write("The contents are: ", doc.to_dict())

docs = db.get()

for doc in docs:
    st.write(f"{doc.id} => {doc.to_dict()}")

st.write([
    doc.id for doc in docs
])