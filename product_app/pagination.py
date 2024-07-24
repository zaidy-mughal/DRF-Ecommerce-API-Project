from rest_framework.pagination import CursorPagination

class CustomPagination(CursorPagination):
    max_page_size = 10
    page_size = 10
    ordering = 'name'
