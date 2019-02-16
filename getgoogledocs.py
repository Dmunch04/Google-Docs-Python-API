from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

DOC_LINK = ['https://www.googleapis.com/auth/documents.readonly']

DOC_ID = '1l_PWJgzBtSgbC6BEGgkFI9nUSeAN6dxq4M4J0AsNrIU'

def get_qotd():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', DOC_LINK)
            creds = flow.run_local_server()
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('docs', 'v1', credentials=creds)

    document = service.documents().get(documentId=DOC_ID).execute()

    return document.get('content')
