from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view


class JWTchemaGenerator(OpenAPISchemaGenerator):
    def get_security_definitions(self):
        return {
            "Bearer": {
                "type": "apiKey",
                "in": "header",
                "name": "Authorization",
                "description": "Format: Bearer <access_token>",
            }
        }


schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version="v1",
        description="E-commerce API",
        contact=openapi.Contact(email="tulqinurinov005@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    generator_class=JWTchemaGenerator,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("apps.user.urls")),
    path("file/", include("apps.file.urls")),
    path("product/", include("apps.product.urls")),
    # Swagger
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
