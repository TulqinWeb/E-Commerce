from rest_framework.routers import DefaultRouter

from apps.file.urls import urlpatterns
from apps.product.views import ProductViewSet

router = DefaultRouter()
router.register(r'', ProductViewSet)
urlpatterns += router.urls
