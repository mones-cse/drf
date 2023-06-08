import json
from django.http import JsonResponse


def api_home(request):
    # * request from django, request -> HttpRequest -> Django
    # * requests from python, requests -> Response -> Python
    print(request.GET)
    body = request.body  # * request.body holdes byte string of json data
    data = {}
    try:
        # * json.loads() converts byte string to python dictionary
        data = json.loads(body)
    except:
        pass
    # * request.headers is metadata of the request
    data['headers'] = dict(request.headers)
    # * request.GET is the query parameters
    data['params'] = dict(request.GET)

    return JsonResponse(data, status=200)

# Create your views here.
