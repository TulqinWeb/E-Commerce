from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from config import settings


class GlobalPagination(PageNumberPagination):
    page_size = getattr(settings, "PAGINATION_PAGE_SIZE", 50)
    page_size_query_param = "page_size"
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response(
            {
                "count": self.page.paginator.count,
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "current_page": self.page.number,
                "page_size": self.page_size,
                "results": data,
            }
        )

