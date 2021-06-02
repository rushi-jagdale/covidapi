from django.shortcuts import render
from rest_framework.response import Response
from .serializers import HospitalSerializer
from rest_framework.decorators import api_view
from . models import Hospital
# Create your views here.


@api_view(['GET'])
def hospitallist(request):
    events = Hospital.objects.all()
    serializer = HospitalSerializer(events, many=True)
    return Response(serializer.data)



  

@api_view(['POST'])
def hospitalCreate(request):
    events = Hospital.objects.all()
    serializer = HospitalSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 

@api_view(['delete'])
def delete(request,pk):
    event = Hospital.objects.get(id=pk)
    event.delete()
    return Response("Deleted")

@api_view(['POST'])
def update(request,pk):
    event = Hospital.objects.get(id=pk)
    serializer = HospitalSerializer(instance=event, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)  

