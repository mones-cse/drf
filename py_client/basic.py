import requests

print('Hello World!')

endpoint = "https://httpbin.org/anything"
endpoint = "http://httpbin.org/status/200"
endpoint = "http://localhost:8000"

get_response = requests.get(endpoint, json={"key": "value"})
print(get_response.text)
print(get_response.status_code)
# {...'data': '{"key": "value"}' ...}

# get_response = requests.get(endpoint, data={"key": "value"})
# print(get_response.json())
# {...'form': '{"key": "value"}' ...}


# https://youtu.be/c708Nf0cHrs?t=1648
