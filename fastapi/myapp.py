import requests
import json

def post_data():
    url="http://127.0.0.1:8000/items"
    data={
        'name':'Akshay',
        'password':'passwordss'
    }
    
    json_data=json.dumps(data)
    r=requests.post(url=url,data=json_data)
    data=r.json()
    print(data)