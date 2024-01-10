from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import Category
from .serializers import *
from rest_framework.generics import ListAPIView
from rest_framework import status



class CategoryAPI(ListAPIView):
     queryset = Category.objects.all()
     serializer_class = CategorySerializer




