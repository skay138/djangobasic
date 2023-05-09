from django.shortcuts import render
from django.http import response
from rest_framework.decorators import api_view
from .models import Test
from rest_framework import serializers

# Create your views here.

class testSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

@api_view(['GET', 'POST'])
def apis_view(request):
    if request.method == 'GET':
        data = Test.objects.all()[:5]
        serializer = testSerializer(data, many=True)
        return response.JsonResponse(serializer.data, safe=False, status=200)
    
    if request.method == 'POST':
        try:
            test = Test.objects.create()
            for keys in request.data:
                if  hasattr(test, keys) == True:
                    setattr(test, keys, request.data[keys])
            test.save()
            return response.HttpResponse(status=201)
        except:
            return response.HttpResponse(status=400)
