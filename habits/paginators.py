from rest_framework.pagination import PageNumberPagination


class HabitPaginator(PageNumberPagination):
    """Pagination for display 5 habits on the page"""
    page_size = 5
