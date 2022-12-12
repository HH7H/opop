
"""
tiktok username chacker
by: NoNeHunter
"""

from flask import Flask
from flask import request
import threading
import colorama
import platform
import requests
import random
import time
import json

app = Flask(__name__)

url = 'https://api2-19-h2.musical.ly/aweme/v1/passport/find-password-via-email/?app_language=ar&manifest_version_code=2018101933&_rticket=1667149902064&iid=7160349471136909061&channel=googleplay&language=ar&fp=&device_type=ANY-LX2&resolution=1080*2298&openudid=39e9b96bb5c6e336&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=480&carrier_region=IQ&ac=wifi&device_id=7116197109661091333&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=HONOR&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233&ts=1667149902&as=a1261b755ea4d3e04e4388&cp=be4a3c6ce5e8520fe1MkUo&mas=0149d8edb9a3340aacd5c82fcadadde3801c1ccc2ca62c0ca6cc26'


headers = {'Host': 'api2-19-h2.musical.ly','Connection': 'keep-alive','Content-Length': '647','Cookie': 'odin_tt=b0db11ac4955afa4589bdb09d8f8fdcf3bcdea5238d0a6e2ba7c6aaea542e8d4ff9a3f324c153df80e03ac5e29a9d411925fa05d2f300713a2295db1eeff68accf50d5ddb5abd11115077fe989cfc094; store-idc=maliva; store-country-code=iq; store-country-code-src=did','Accept-Encoding': 'gzip','X-SS-QUERIES': 'dGMCAr6ot3awALq2qSjedy1Vk99nIoud%2BAhHSPAsj5dyUWFbxRx0wm95EoKwwNB3VVlOMd4SzMIENA51cwBS%2Bm0N1T95yguPVZ4OunAWAs0t0bHbsPclnVdl1Uh%2BLGZVXFGTew%3D%3D','sdk-version': '1','Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8','X-SS-TC': '0','User-Agent': 'com.zhiliaoapp.musically/2018101933 (Linux; U; Android 11; ar_IQ_#u-nu-latn; ANY-LX2; Build/HONORANY-L22CQ; Cronet/58.0.2991.0)'}

@app.route('/')
def Root():
    return 'tele: @NkNkER'


@app.route('/email/checkavail/')
def Checker():
    email = str(request.args.get('email'))
    data = f'app_language=ar&manifest_version_code=2018101933&_rticket=1667150564079&iid=7160349471136909061&channel=googleplay&language=ar&fp=&device_type=ANY-LX2&resolution=1080*2298&openudid=39e9b96bb5c6e336&update_version_code=2018101933&sys_region=IQ&os_api=30&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=480&email={email}&retry_type=no_retry&carrier_region=IQ&ac=wifi&device_id=7116197109661091333&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=880&carrier_region_v2=418&app_name=musical_ly&ab_version=8.8.0&version_name=8.8.0&device_brand=HONOR&ssmix=a&pass-region=1&build_number=8.8.0&device_platform=android&region=SA&aid=1233'

    response = requests.post(url=url,headers=headers, data=data).text
    
    if 'Sent successfully' in response:
        returned = json.dumps({"status": "ok","isAvailable": True,"email": email, "type": "TikTok"})
    
    elif 'Bind device by email failed' in response:
        returned = json.dumps({"status": "ok","isAvailable": False,"email": email, "type": "TikTok"})
    elif 'Sorry, you sent email too often' in response:
        returned = json.dumps({"status": "ok","isAvailable": False,"email": email, "type": "TikTok"})
        
    else:
        returned = json.dumps({"status": "error","isAvailable": "None","email": email, "type": "TikTok"})
    return returned
