import requests

url = 'http://localhost:5000/upload'
files = {'file': open('example.txt', 'rb')}  # replace with your file
response = requests.post(url, files=files)

print(response.status_code)
print(response.text)
