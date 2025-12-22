from rest_framework.viewsets import ModelViewSet

from apps.common.core.services.pagination import GlobalPagination
from apps.file.models import File
from apps.file.serializers import FileSerializer


class FileViewSet(ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    pagination_class = GlobalPagination
