from django.shortcuts import render
from .models import Questions
from .serializers import AnswerSerializer
from rest_framework.views import APIView, Response
from rest_framework import status
from .paginations import CustomPagination
from  django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.generics import GenericAPIView, ListAPIView
from django.core.paginator import Paginator
from config import settings
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import NotFound as NotFoundError


#
#
# class QuestionsAPI(ListAPIView):
#     pagination_class = CustomPagination
#     serializer_class = AnswerSerializer
#
#
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['questions', 'answers']
#
#
#     def get_queryset(self):
#         Talent = Questions.objects.all()
#         return Talent





class QuestionsAPI(APIView, CustomPagination):
     serializer_class = AnswerSerializer

     def get(self,request):
         try:
            end = Questions.objects.all()
            results = self.paginate_queryset(end, request, view=self)
            serializer = AnswerSerializer(results, many=True)
            return self.get_paginated_response(serializer.data)

         except Exception as e:
             print(e)

         return Response({"status":status.HTTP_404_NOT_FOUND})

#
#
# class CustomPaginator(PageNumberPagination):
#     page_size = 3
#
#     def generate_response(self, query_set, serializer_obj, request):
#         try:
#             page_data = self.paginate_queryset(query_set, request)
#         except NotFoundError:
#             return Response({"error": "No results found for the requested page"},
#                             status=status.HTTP_400_BAD_REQUEST)
#
#         serialized_page = serializer_obj(page_data, many=True)
#         return self.get_paginated_response(serialized_page.data)
#
# #
# #
# #
# class QuestionsAPI(APIView):
#
#     def get(self, request, format=None):
#         try:
#            cart_details = Questions.objects.all()
#            paginator = CustomPaginator()
#            response = paginator.generate_response(cart_details, AnswerSerializer, request)
#            return response
#
#         except Exception as e:
#                   print(e)
#
#
#         return Response({"status":status.HTTP_404_NOT_FOUND})