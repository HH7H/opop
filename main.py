from flask import Flask,request
import requests

API = Flask(__name__)

@API.route('/')
def Root():
    return 'Welcome'

URL = 'https://www.instagram.com/accounts/check_email/'

Headers = {'Host': 'www.instagram.com','Accept': '*/*','X-ASBD-ID': '198387','X-Requested-With': 'XMLHttpRequest','X-IG-App-ID': '1217981644879628','X-Instagram-AJAX': '542bd73aee81','Accept-Language': 'en-US,en;q=0.9','Accept-Encoding': 'gzip, deflate, br','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://www.instagram.com','User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1','Referer': 'https://www.instagram.com/accounts/signup/email','X-IG-WWW-Claim': '0','Content-Length': '26','Connection': 'keep-alive','Cookie': 'csrftoken=Am2ApnZ7OPwA4qVbdbkGHinL2vdT8oE1; ig_did=601DC320-7C26-4CEC-B87B-15F7AC855219; ig_nrcb=1; mid=YvtnAgAAAAEiRteTqWs3Is1lFcBV','X-CSRFToken': 'Am2ApnZ7OPwA4qVbdbkGHinL2vdT8oE1'}

@API.route('/instagram/email/available/email=<email>')
def Checker(email):
    Data = {'email': email}
    Response = requests.post(URL,headers=Headers,data=Data).text
    return Response


