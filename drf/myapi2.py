import requests,json

URL = 'http://127.0.0.1:8000/deserial_api/stu_create/'

data = {
    'name':'Cavi',
    'roll':102,
    'city':'Dydeny',
} 

json_data = json.dumps(data)  # Python dict  to Json

r = requests.post(url=URL,data=json_data)

# This is optional 
jdata = r.json()
print(jdata)