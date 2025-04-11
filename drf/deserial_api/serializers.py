from rest_framework import serializers
from deserial_api.models import Student

class StudentSerializers(serializers.Serializer):
    
    name = serializers.CharField(max_length=20)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=10)

    def create(self, validate_data):
        return Student.objects.create(**validate_data)

    # Field label Validation
    def validate_roll(self,value):  # validate_fieldname = validation for single field
        if(value > 200):
            raise serializers.ValidationError('Seat Full')
        return value 
    
    # Object level validation =  validate () => for all field validation
    def validate(self,data):
        nm = data.get('name')
        ct = data .get('city')

        if (nm[0].islower() or ct[0].islower()):
            raise serializers.ValidationError("Must be Uppercase")
        
        return data