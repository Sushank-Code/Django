import requests,json

URL = 'http://127.0.0.1:8000/model_serializer/model_info/'

data = {
    'username':'Sonam',
    'email':'sonam1234@gmail.com',
    'gender':'F'
} 

json_data = json.dumps(data)  # Python dict  to Json

r = requests.post(url=URL,data=json_data)

jdata = r.json()
print(jdata)