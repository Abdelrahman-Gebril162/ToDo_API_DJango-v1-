from django.http.response import JsonResponse
from django.shortcuts import render

#this you need if you will work with function based view
#allow you to use api_view Decorator @api_view([request_method])
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

from .models import Task
# Create your views here.

@api_view(['GET'])
def ApiOverView(request):
    #When we make Safe=True that means
    #that we should pass a dictionaty object 
    #so that it can be serialized or conveted to json object
    #code to check->return JsonResponse("API BASED POINT", safe=False)

    #this is a collection of services I will make in api
    api_urls = {
        "list":"/task_list/",
        "Details":"/task_details/<str:pk>/",
        "Create":"/tesk_create/",
        "Update":"/task_update/<str:pk>/",
        "Delete":"/task_delete/<str:pk>/"
    }

    #this will preview the collection in the rest_framework built_in view
    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):
    #this will git the data in queryset formate
    tasks = Task.objects.all()

    #this will convert the queryset formate to json
    #to make it visible to browser
    #many=True -> means we will retraive list of objects
    sr = TaskSerializer(tasks,many=True)
    return Response(sr.data)

@api_view(['GET'])
def taskDetail(request,pk):
    tasks=Task.objects.get(id=pk)
    sr = TaskSerializer(tasks,many=False)
    return Response(sr.data)

@api_view(['POST'])
def taskCreate(request):
    sr = TaskSerializer(data=request.data)
    if sr.is_valid():
        sr.save()
        return Response("Created Successfully")
    else:
        return(sr.errors)

@api_view(['PUT'])
def taskUpdate(request,pk):
    tasks=Task.objects.get(id=pk)
    sr = TaskSerializer(instance=tasks,data=request.data)
    if sr.is_valid():
        sr.save()
        return Response(sr.data)
    else:
        return Response(sr.errors)

@api_view(['DELETE'])
def taskDelete(request,pk):
    tasks=Task.objects.get(id=pk)
    tasks.delete()
    return Response("Deleted Successfully")

