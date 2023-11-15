import requests

res = requests.get('http://127.0.0.1:3000/api/courses/0')
print(res.json())
#res = requests.post('http://127.0.0.1:3000/api/courses/4', {"name": "C#", "videos": 20})
#print(res.json())
