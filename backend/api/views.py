from django.http import JsonResponse


def api_home(request):
    return JsonResponse({"message": "HI THERE!"}, status=200)

# Create your views here.
