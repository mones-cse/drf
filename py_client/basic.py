import requests

print('Hello World!')

endpoint = "https://httpbin.org/anything"
endpoint = "http://httpbin.org/status/200"
endpoint = "http://localhost:8000/api/"

get_response = requests.get(
    endpoint, json={"JSON": "value"}, params={"PARAMS": "value"})
print(get_response.status_code)
print(get_response.json())


# * If we send json parameter to the endpoint, we get data in the json key of the response.
# get_response = requests.get(endpoint, json={"key": "value"})
# print(get_response.json())
# {...'data': '{"key": "value"}' ...}

# * If we send data parameter to the endpoint, we get data in the form key of the response.
# get_response = requests.get(endpoint, data={"key": "value"})
# print(get_response.json())
# {...'form': '{"key": "value"}' ...}

# * get_response.text shows us the raw response.
