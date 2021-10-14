from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from  .models import  Post
from .serializers import SnippetSerializer


@api_view(['get'])
def hello_world(request):
    set = Post.objects.all().order_by('-id')
    sertializer = SnippetSerializer(set,many=True)
    return Response(sertializer.data)


@api_view(['GET'])
def detail(request,id):
    set = Post.objects.get(id=id)
    sertializer = SnippetSerializer(set,many=False)
    return Response(sertializer.data)

@api_view(['POST'])
def create(request):
    sertializer = SnippetSerializer(data=request.data)
    if sertializer.is_valid():
        sertializer.save()
    return Response(sertializer.data)

@api_view(['POST'])
def update(request,id):
    set = Post.objects.get(id=id)
    sertializer = SnippetSerializer(instance=set, data=request.data)
    if request.method == "POST":
     if sertializer.is_valid():
        sertializer.save()
    return Response(sertializer.data)

@api_view(['DELETE'])
def delete(request,id):
    set = Post.objects.get(id=id)
    set.delete()
    return Response("item berhasil di hapus")
