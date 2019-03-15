# encoding: utf-8
import requests

def get_token(username, password, url):
    Token = ""
    login_headers = {'Content-Type': 'application/json'}
    data = dict(username=username, password=password)
    login_res = requests.post(url=url, json=data, headers=login_headers)
    login_token = login_res.headers[Token]
    return login_token

