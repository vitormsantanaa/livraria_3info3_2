from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from core.models import Livro, Compra 
from core.serializers import (
    LivroAlterarPrecoSerializer,
    LivroListSerializer,
    LivroSerializer,
    LivroListRetrieveSerializer,
    LivroMaisVendidoSerializer,
    LivroAjustarEstoqueSerializer,
)
from drf_spectacular.utils import OpenApiResponse, extend_schema
from django.db.models import Q, Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer  

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categoria__descricao', 'editora__nome']

    @extend_schema(
        summary="Ajusta o estoque de um livro",
        description="Aumenta ou diminui o estoque; impede resultado negativo.",
        request=LivroAjustarEstoqueSerializer,
        responses={
            200: OpenApiResponse(
                response=None,
                description="Estoque ajustado com sucesso.",
                examples=[
                    {
                        "status": "Quantidade ajustada com sucesso",
                        "novo_estoque": 30
                    }
                ]
            ),
            400: OpenApiResponse(
                description="Erro de validação",
                examples=[
                    {"quantidade": "A quantidade em estoque não pode ser negativa."}
                ]
            ),
        },
        )
    @action(detail=True, methods=['post'])
    def ajustar_estoque(self, request, pk=None):
        livro = self.get_object()

        serializer = LivroAjustarEstoqueSerializer(data=request.data, context={'livro': livro})
        serializer.is_valid(raise_exception=True)

        quantidade_ajuste = serializer.validated_data['quantidade']
        livro.quantidade += quantidade_ajuste
        livro.save()

        return Response(
            {'status': 'Quantidade ajustada com sucesso', 'novo_estoque': livro.quantidade},
            status=status.HTTP_200_OK
        )
