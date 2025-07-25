import json

with open('client_secret.json') as f:
    data = json.load(f)


client_id = data['client_id']
redirect_uri = data['redirect_uris'][0]
auth_url = (
    "https://accounts.google.com/o/oauth2/v2/auth?"
    f"client_id={client_id}&"
    f"redirect_uri={redirect_uri}&"
    "response_type=code&"
    "scope=https://www.googleapis.com/auth/forms&"
    "access_type=offline&"
    "prompt=consent"
)