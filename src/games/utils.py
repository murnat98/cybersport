from django.core.exceptions import FieldDoesNotExist
from rest_framework.pagination import PageNumberPagination


class DefaultPagination(PageNumberPagination):
    """
    Default class for pagination with page size 10.
    """
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 3


class QuerySetOrderingMixin:
    """
    Overrides get_queryset for getting, which gets sort as get parameter and sorting.
    """
    model = None

    def get_queryset(self):
        """
        :return: queryset ordered by sort parameter from GET request
        """
        sort_parameter = 'name'
        if 'sort' in self.request.GET:
            sort_parameter = self.request.GET['sort']

        try:
            self.model._meta.get_field(sort_parameter)
        except FieldDoesNotExist:
            return self.model.objects.all()

        return self.model.objects.all().order_by(sort_parameter)
