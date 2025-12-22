from rest_framework.viewsets import ModelViewSet

from apps.common.core.permissions.custom_permissions import IsAdminOrReadOnly
from apps.common.core.services.pagination import GlobalPagination
from apps.product.models import Product
from apps.product.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = GlobalPagination
    # permission_classes = [IsAdminOrReadOnly]
