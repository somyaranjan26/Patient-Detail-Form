import requests

url = 'http://127.0.0.1:5000/predict_api'
r = requests.post(url,json={'gender':1, 'age':0, 'Heart_rate':8})

print(r.json())