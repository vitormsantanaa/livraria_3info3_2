from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter

from core.models import Autor
from core.serializers import AutorSerializer


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

    filter_backends = [OrderingFilter]
    ordering_fields = ['nome']
    ordering = ['nome']