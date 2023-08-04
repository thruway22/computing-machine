import json
from google.cloud import firestore
from google.oauth2 import service_account

def service_account():
    return service_account.Credentials.from_service_account_info(json.loads(st.secrets['textkey']))

def client():
    return firestore.Client(credentials=service_account(), project='my-family-fund')

def db():
    return client().collection('holdings')

db = db()

