from django.core.exceptions import FieldDoesNotExist
from django.db import models
from rest_framework.pagination import PageNumberPagination


class DefaultPagination(PageNumberPagination):
    """
    Default class for pagination with page size 10.
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


class QuerySetOrderingMixin:
    """
    Overrides get_queryset for getting, which gets sort as get parameter and sorting.
    """
    model = None
    default_sort_parameter = 'name'

    def get_sort_parameter(self):
        sort_parameter = self.default_sort_parameter
        if 'sort' in self.request.GET:
            sort_parameter = self.request.GET['sort']

        try:
            assert issubclass(self.model, models.Model)
            self.model._meta.get_field(sort_parameter)
        except FieldDoesNotExist:
            sort_parameter = self.default_sort_parameter

        return sort_parameter

    def is_desc(self):
        return 'desc' in self.request.GET

    def get_queryset(self):
        """
        :return: queryset ordered by sort parameter from GET request
        """
        sort_parameter = self.get_sort_parameter()

        if self.is_desc():
            sort_parameter = '-%s' % sort_parameter

        return self.model.objects.all().order_by(sort_parameter)
