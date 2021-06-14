from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import StudentSerializer

# Create your views here.

@api_view(['GET'])
def list(r):
    std = Student.objects.all()
    ser = StudentSerializer(std, many =True)
    return Response(ser.data)


@api_view(['POST'])
def create(r):
    ser = StudentSerializer(data = r.data)
    if ser.is_valid():
        ser.save()
    return Response(ser.data)


@api_view(['DELETE'])
def delete(r, pk):
    std = Student.objects.get(id=pk)
    std.delete()
    return Response('Delete')


@api_view(['GET'])
def listdetails(r, pk):
    std = Student.objects.get(id = pk)
    ser = StudentSerializer(std, many=False)
    return Response(ser.data)


@api_view(['POST'])
def update(r, pk):
    std = Student.objects.get(id=pk)
    ser = StudentSerializer(instance=std, data=r.data)
    if ser.is_valid():
        ser.save()
    return Response(ser.data)