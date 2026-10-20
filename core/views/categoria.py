from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter

from core.models import Editora
from core.serializers import EditoraSerializer


class EditoraViewSet(ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer

    filter_backends = [OrderingFilter]
    ordering_fields = ['nome']
    ordering = ['nome']