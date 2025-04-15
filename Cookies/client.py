import requests

# Create a session to persist cookies
session = requests.Session()

# 1. Set a cookie
response = session.get('http://localhost:5000/set_cookie/Shraddha')
print("[SET] ", response.text)

# 2. Access homepage to see greeting with cookie
response = session.get('http://localhost:5000/')
print("[GET with Cookie] ", response.text)

# 3. Delete the cookie
response = session.get('http://localhost:5000/delete_cookie')
print("[DELETE] ", response.text)

# 4. Access homepage again after cookie deletion
response = session.get('http://localhost:5000/')
print("[GET after Deletion] ", response.text)
