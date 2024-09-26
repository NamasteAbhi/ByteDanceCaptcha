import requests

RapidApiKey = "" #Enter Your Rapid Key Here

payload = {
    "proxy": "username:password@host:port", #Use Proxy In Same Format
    "endpoint": "rc-verification16-normal-useast5.tiktokv.us",
    "iid": "7383569631618991878",
    "device_id": "7366359272542291461",
    "region": "us",
    "VerifyFp": "" #For App No Need VerifyFp Token But For Web You Need
}
headers = {
    "x-rapidapi-key": RapidApiKey,
    "x-rapidapi-host": "bytedancecaptcha.p.rapidapi.com",
    "Content-Type": "application/json"
}

response = requests.post("https://bytedancecaptcha.p.rapidapi.com/Slide_Captcha/", json=payload, headers=headers)

print(response.json())
