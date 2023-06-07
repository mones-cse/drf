import requests

print('Hello World!')

endpoint = "https://httpbin.org/anything"
endpoint2 = "http://httpbin.org/status/200"

get_response = requests.get(endpoint, json={"key": "value"})
print(get_response.json())
# {...'data': '{"key": "value"}' ...}

get_response = requests.get(endpoint, data={"key": "value"})
print(get_response.json())
# {...'form': '{"key": "value"}' ...}
