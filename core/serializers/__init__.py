from .autor import AutorSerializer
from .categoria import CategoriaSerializer
from .editora import EditoraSerializer
from .user import UserRegistrationSerializer, UserSerializer
from .livro import (
    LivroAlterarPrecoSerializer,
    LivroListSerializer,
    LivroRetrieveSerializer,
    LivroSerializer,
)
from .compra import (
    CompraCreateUpdateSerializer,
    CompraListSerializer, 
    CompraSerializer,
    ItensCompraCreateUpdateSerializer,
    ItensCompraListSerializer, 
    ItensCompraSerializer,
)