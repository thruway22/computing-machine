import json
import streamlit as st
from google.cloud import firestore
from google.oauth2 import service_account

def get_service_account(credentials_info):
    return service_account.Credentials.from_service_account_info(json.loads(credentials_info))

def get_client(credentials_info, project):
    return firestore.Client(credentials=get_service_account(credentials_info), project=project)

def get_db(credentials_info, project, collection):
    return get_client(credentials_info, project).collection(collection)

db = get_db(st.secrets['textkey'], 'my-family-fund', 'holdings')

