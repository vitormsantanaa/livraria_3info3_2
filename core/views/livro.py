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
)
from drf_spectacular.utils import extend_schema
from django.db.models import Q, Sum

class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer  # Seu serializer padrão

    @extend_schema(
        summary="Lista os livros mais vendidos",
        description="Retorna os livros que venderam mais de 10 unidades.",
        responses={
            200: LivroMaisVendidoSerializer(many=True)
        },
    )
    @action(detail=False, methods=['get'])
    def mais_vendidos(self, request):
        livros = Livro.objects.annotate(
            total_vendidos=Sum(
                'itens_compra__quantidade',
                filter=Q(itens_compra__compra__status=Compra.StatusCompra.FINALIZADO)
            )
        ).filter(total_vendidos__gt=10).order_by('-total_vendidos')

        serializer = LivroMaisVendidoSerializer(livros, many=True)

        if not serializer.data:
            return Response(
                {"detail": "Nenhum livro excedeu 10 vendas."},
                status=status.HTTP_200_OK
            )

        return Response(serializer.data, status=status.HTTP_200_OK)
