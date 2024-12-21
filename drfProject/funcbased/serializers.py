from rest_framework import serializers


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    age = serializers.IntegerField(default=10)
    email = serializers.EmailField()
