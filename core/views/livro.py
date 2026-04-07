from rest_framework.viewsets import ModelViewSet
from core.models import Livro 
from core.serializers import LivroListRetrieveSerializer, LivroSerializer, LivroListSerializer

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

def get_serializer_class(self):
    if self.action == 'list':
        return LivroListSerializer
    elif self.action == 'retieve':
        return LivroListRetrieveSerializer
    return LivroSerializer