import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
# See https://developers.google.com/identity
# for guides on implementing OAuth2 for the application.
  
# If changing scope, delete token.json

SLIDES = {
    "SCOPES" : ["https://www.googleapis.com/auth/presentations"],
    "ID" : ""
        }

SHEETS = {
    "SCOPES": ["https://www.googleapis.com/auth/spreadsheets"], 
    "ID" : "",
    "DATARANGE" : "A1:B5"
        }



def get_credentials_slides():
    creds = None
    if os.path.exists("token_sl.json"):
        creds = Credentials.from_authorized_user_file("token_sl.json", SLIDES["SCOPES"])
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json",SLIDES["SCOPES"])
            creds = flow.run_local_server(port=0)
        with open("token_sl.json", "w") as token:
            token.write(creds.to_json())
    return creds

def get_credentials_sheets():
    creds = None
    if os.path.exists("token_sh.json"):
        creds = Credentials.from_authorized_user_file("token_sh.json", SHEETS["SCOPES"])
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json",SHEETS["SCOPES"])
            creds = flow.run_local_server(port=0)
        with open("token_sh.json", "w") as token:
            token.write(creds.to_json())
    return creds