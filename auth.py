import json
import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account

# def get_service_account():
#     return service_account.Credentials.from_service_account_info(json.loads(st.secrets['textkey']))

# def get_client():
#     return firestore.Client(credentials=get_service_account(), project='my-family-fund')

# def get_db():
#     return get_client().collection('holdings')

# db = db()

class Database:
    def __init__(self):
        self.key = st.secrets['textkey']
        self.credentials = service_account.Credentials.from_service_account_info(json.loads(self.key))
        self.client = firestore.Client(credentials=self.credentials, project='my-family-fund')
        self.db = self.client.collection('holdings')

    def get_db():
        return self.db

