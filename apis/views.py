from django.shortcuts import render
from django.http import response

# Create your views here.


def apis_view(request):
    if request.method == 'GET':
        data = {
            "author" : "sangkyu",
            "content" : "he is studying django"
        }
        return response.JsonResponse(data, safe=False)
    
