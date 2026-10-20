from .autor import AutorSerializer
from .categoria import CategoriaSerializer
from .editora import EditoraSerializer
from .user import UserRegistrationSerializer, UserSerializer
from .livro import (
    LivroAlterarPrecoSerializer,
    LivroListSerializer,
    LivroListRetrieveSerializer,
    LivroMaisVendidoSerializer,
    LivroSerializer,
    LivroAjustarEstoqueSerializer,
)
from .compra import (
    CompraCreateUpdateSerializer,
    CompraListSerializer, 
    CompraSerializer,
    ItensCompraCreateUpdateSerializer,
    ItensCompraListSerializer, 
    ItensCompraSerializer,
)