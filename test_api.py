import requests

api_url = "http://127.0.0.1:5000/check_url"  # Change this if API is deployed online
test_data = {"url": "http://malicious-site.com"}

response = requests.post(api_url, json=test_data)
print("Response:", response.json())