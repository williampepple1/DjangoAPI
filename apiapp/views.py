from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


from .serializers import StudentSerializer
from .models import Student

# Create your Views here.
class FirstView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Student.objects.all()
        serializer = StudentSerializer(qs, many=True)
        return Response(serializer.data)

class SecondView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Student.objects.all()
        serializer = StudentSerializer(qs, many=True)
        return Response(serializer.data)
