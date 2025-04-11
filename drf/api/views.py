from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from api.models import Contact
from api.serializers import ContactSerializers
from rest_framework.renderers import JSONRenderer

# Create your views here.
def contact_view(request,pk):
    con = Contact.objects.get(id = pk) # getting data form database

    serial_data = ContactSerializers(con) # converting complex model to native python
    json_data = JSONRenderer().render(serial_data.data) # python to Json
    print(json_data)
    return HttpResponse(json_data,content_type = 'application/json')

# Query set - all data
def contact_view_all(request):
    con = Contact.objects.all()

    serial_data = ContactSerializers(con,many = True)  
    return JsonResponse(serial_data.data,safe=False) # safe is true by default
    # safe must be false inorder to parse no dict object to Json

    # json_data = JSONRenderer().render(serial_data.data) 
    # print(json_data)
    # return HttpResponse(json_data,content_type = 'application/json')

