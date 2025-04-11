from rest_framework import serializers

class ContactSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20)
    email = serializers.EmailField(max_length=20)
    phone = serializers.CharField(max_length=10)
    
    