import json
from django.http import JsonResponse
from products.models import Product

# Create your views here.


def api_home(request):
    product_data = Product.objects.all().order_by("?").first()
    print(product_data)
    data = {}
    if product_data:
        data['id'] = product_data.id
        data['title'] = product_data.title
        data['content'] = product_data.content
        data['price'] = product_data.price

    return JsonResponse({"data": data})


def api_echo_back(request):
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
