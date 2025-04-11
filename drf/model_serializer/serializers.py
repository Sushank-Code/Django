from rest_framework import serializers
from model_serializer.models import Info

class InfoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Info
        fields = ['id','username','email','gender']
        read_only_fields = ['gender']
