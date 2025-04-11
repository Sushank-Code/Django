from django.shortcuts import render
import io
from django.http import JsonResponse,HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from deserial_api.serializers import StudentSerializers
from deserial_api.models import Student
from django.views.decorators.csrf import csrf_exempt   # Ignoring csrf

# Create your views here.

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body    # Give Raw data
        stream = io.BytesIO(json_data)  
        python_data = JSONParser().parse(stream) # parse stream to python dict
        serializer = StudentSerializers(data = python_data) # into native python

        if serializer.is_valid():       
            serializer.save()   # save into database as models(complex dataType)
            res = {'msg' : 'Data inserted'}
            return JsonResponse(res)
        
        return JsonResponse(serializer.errors)
