# https://www.dropbox.com/oauth2/authorize?client_id=<APP_KEY>&token_access_type=offline&response_type=code

# sl.Bm73n-LQcSlV_Pj2pUm_ksfT7ixjNnMNFf-Tb_sbbwWrtC7kLVs_c_F2BMOS8vthVdgMIlisWR0_JWislE0n7EwVBbVUAsmapmVkPSCmB-USlb6zsz2zsvdtMinC2d3XcpoVSP4Rcgkn

import base64
import requests
import json

APP_KEY = 'hvr42e05zuhwium'
APP_SECRET = 'asewtnhbuglulua'
ACCESS_CODE_GENERATED = 'XHAKhEBbrBAAAAAAAABHG-DRwidYKss6lvRzOpyTG2M'

BASIC_AUTH = base64.b64encode(f'{APP_KEY}:{APP_SECRET}'.encode())

headers = {
    'Authorization': f"Basic {BASIC_AUTH}",
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = f'code={ACCESS_CODE_GENERATED}&grant_type=authorization_code'

response = requests.post('https://api.dropboxapi.com/oauth2/token',
                         data=data,
                         auth=(APP_KEY, APP_SECRET))
print(json.dumps(json.loads(response.text), indent=2))