
from.serializers import StudentSerializer
from .models import StudentModel

from rest_framework.viewsets import ModelViewSet

# Create your views here.



from rest_framework.views import APIView
from rest_framework.response import Response


class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message":"Hello World!"})
    
    def post(self, request):
        name = request.data.get("name")
        if not name:
            return Response({"error":"No name Passed"})
        return Response({"message": f"hello{name}!"})
    


# class StudentView(APIView):
#     def get(self, request):
#         return Response({"message":"Hello Students!"})

#     def post(self, request):
#         serializer = StudentSerializer(data = request.data)
#         if serializer.is_valid():
#             valid_data = serializer.data

#             name = valid_data.get("name")
#             age = valid_data.get("age")

#             return Response({"message":f"hello {name}, you're {age} years old"})
#         else:
#             return Response({"errors":serializer.errors})
        

# class StudentView(APIView):
#     def get(self, request):
#         student_data = StudentModel.objects.all()
#         serializer_student = StudentSerializer(student_data, many = True)
#         return Response(serializer_student.data)

#     def post(self, request):
#         serializer = StudentSerializer(data = request.data)
#         if serializer.is_valid():
#            print(serializer.data)
#            student_instance = StudentModel.objects.create(**serializer.data)

#            return Response({"message":f"Created succefully {student_instance.id}"})
#         else:
#             return Response({"errors":serializer.errors})





class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = StudentModel.objects.all()