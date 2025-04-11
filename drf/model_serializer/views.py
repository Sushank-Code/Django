from django.shortcuts import render
import io
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from model_serializer.serializers import InfoSerializer
from django.views.decorators.csrf import csrf_exempt   

# Create your views here.

@csrf_exempt
def Info_create(request):
    if request.method == 'POST':
        json_data = request.body   
        stream = io.BytesIO(json_data)  
        python_data = JSONParser().parse(stream) 
        serializer = InfoSerializer(data = python_data) 

        if serializer.is_valid():       
            serializer.save()   
            res = {'msg' : 'Data inserted'}
            return JsonResponse(res)
        
        return JsonResponse(serializer.errors)

