from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from .models import EmployeeModel




# @api_view(["GET", "POST"])
# def EmployeeView(request):
#     if request.method == "GET":
#         return Response({"message":"hello this is get method"})
#     else:
#         serializers = EmployeeSerializer(data = request.data)
#         if serializers.is_valid():
#             data_valid = serializers.data
            
#             name = data_valid.get("name")
#             age = data_valid.get("age")
#             email = data_valid.get("email")
#             return Response({"message":f"Employee name is {name}, age =  {age} and email =  {email}"})
        
#         return Response({"error":serializers.errors})



@api_view(['GET', 'POST'])
def EmployeeView(request):
    if request.method == "GET":
        employee = EmployeeModel.objects.all()
        serializers = EmployeeSerializer(employee, many=True)
        return Response(serializers.data)
    else:
        serializers = EmployeeSerializer(data = request.data)
        if serializers.is_valid():
            employee = EmployeeModel.objects.create(**serializers.data)
            return Response({"message":f"{employee.id} is successfully created"})
        return Response({"message":serializers.errors})
        

        

