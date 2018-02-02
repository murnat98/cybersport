from rest_framework import viewsets

from api_v0_1.utils import QuerySetOrderingMixin, DefaultPagination


class DefaultAPIView(QuerySetOrderingMixin, viewsets.ModelViewSet):
    pagination_class = DefaultPagination
    list_serializer_class = None
    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'list':
            return self.list_serializer_class

        return self.detail_serializer_class
