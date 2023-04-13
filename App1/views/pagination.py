from rest_framework.pagination import PageNumberPagination


class PageNumberCustomPagination(PageNumberPagination):
    page_size = 100                # TODO : Standard page size
    max_page_size = 100            # TODO : Max Page Size
    page_size_query_param = 'size'  # TODO : No. of records to display in one page
    page_query_param = 'page'       # TODO : Page number
