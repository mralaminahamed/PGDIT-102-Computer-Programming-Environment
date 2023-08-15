import requests

url = 'https://maps.googleapis.com/maps/api/geocode/json'
params = {'sensor': 'false', 'address': 'Mountain View, CA'}
response = requests.get(url, params=params)
result = response.json()

if 'error_message' in result:
    print('Status:', result['status'])
    print('Message:', result['error_message'])
else:
    print(result)
    # print(results)
    # location = results[0]['geometry']['location']
    # print(location['lat'], location['lng'])
