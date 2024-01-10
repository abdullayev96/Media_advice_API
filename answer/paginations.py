from rest_framework.pagination import PageNumberPagination



class CustomPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000




# class CustomPaginator(PageNumberPagination):
#     page_size = 2
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