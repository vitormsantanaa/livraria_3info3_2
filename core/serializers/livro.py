from rest_framework.serializers import (
    DecimalField,
    ModelSerializer,
    Serializer,
    SlugRelatedField,
    ValidationError,
)
from core.models import Livro 

class LivroListRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'
        depth = 1

class LivroListSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = {'id', 'titulo', 'preco'}

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro 
        fields = '__all__'

class LivroAlterarPrecoSerializer(Serializer):
    preco = DecimalField(max_digits=7, decimal_places=2)

    def validate_preco(self, preco):
        '''Valida se o preço é um valor positivo.'''
        if preco <= 0:
            raise ValidationError('O preço deve ser um valor positivo.')
        return preco