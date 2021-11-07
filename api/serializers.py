#this file will make us convert our Models to 
#the Json formate and vice verse
#to make it seen in the browser or work with it in python

from django.db.models import fields
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"