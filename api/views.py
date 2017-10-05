from api.serializers import TestSerializer
from rest_framework import viewsets


class TestViewSet(viewsets.ViewSet):
    serializer_class = TestSerializer
