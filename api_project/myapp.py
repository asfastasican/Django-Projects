import requests
import json


def get_data(id=None):
    url="http://127.0.0.1:8000/studentapi/"
    data={}
    if id is not None:
        data = {'id':id}
    json_data=json.dumps(data)
    print(json_data)
    r=requests.get(url=url,data=json_data)
    data=r.json()
    print(data)
    
#get_data(2)  for GEtting the Data


def post_data():
    url="http://127.0.0.1:8000/stucreate/"
    data={
        'name':'Vallabh',
        'roll':6,
        'city':'Gulbarga'
    }
    
    json_data=json.dumps(data)
    r=requests.post(url=url,data=json_data)
    data=r.json()
    print(data)
    
#post_data()

def partial_update_data():
    url="http://127.0.0.1:8000/stupatch/"
    data={
        'id': 5,
        'name':'Saurabh',
        'roll':6,
        'city':'Uruli'
    }
    
    json_data=json.dumps(data)
    r=requests.put(url=url,data=json_data)
    data=r.json()
    print(data)
    
#partial_update_data()

def update_data():
    url="http://127.0.0.1:8000/stupdate/"
    data={
        'id': 4,
        'name':'Praveen',
        'roll':7,
        'city':'Indapur'
    }
    
    json_data=json.dumps(data)
    r=requests.put(url=url,data=json_data)
    data=r.json()
    print(data)
    
#update_data()


#For Deleting the Data
def delete_data():
    url="http://127.0.0.1:8000/studel"
    data={'id':5}
    json_data=json.dumps(data)
    r=requests.delete(url=url,data=json_data)
    data=r.json()
    print(data)
delete_data()