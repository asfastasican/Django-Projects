import json

"""

python_data={'name':'Akshay','id':1}
print(type(python_data))
print(python_data)
json_data=json.dumps(python_data)
print(type(json_data))
print(json_data)

print("------------------------------")

print(type(json_data))
print(json_data)
parsed_data=json.loads(json_data)
print(type(parsed_data))
print(parsed_data)

"""

"""
# for getting the data
import requests
URL="http://127.0.0.1:8000/api/student_list/"
r=requests.get(url=URL)
data=r.json()
print(data)

"""

""""
#for Posting the data
import requests
import json
URL="http://127.0.0.1:8000/api/student_create/"
data={
    'id':5,
    'name':'Rohini',
    'roll':106,
    'city':'Baramati'
}
json_data=json.dumps(data)
r=requests.post(url=URL,data=json_data)
data=r.json()
print(data)

"""
## for getting the data
import requests

URL="http://127.0.0.1:8000/api/student_get"
def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    data=r.json()
    print(data)
    
    
get_data()