from rest_framework import serializers
from .models import StudentModel

# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(required = True , max_length =100)
#     age = serializers.IntegerField(required = False, min_value = 10, default = 10)
#     email = serializers.EmailField()



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = "__all__"