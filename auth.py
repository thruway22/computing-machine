import json
import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account

class Database:
    def __init__(self):
        self.key = json.loads(st.secrets['textkey'])
        self.credentials = service_account.Credentials.from_service_account_info(self.key)
        self.client = firestore.Client(credentials=self.credentials, project='my-family-fund')
        self.db = self.client.collection('holdings')