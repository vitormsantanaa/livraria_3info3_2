from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from core.models import Livro

class LivroListRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro 
        fields = '__all__'