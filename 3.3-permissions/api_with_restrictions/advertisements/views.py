from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Advertisement
from .serializers import AdvertisementSerializer
from django_filters.rest_framework import DjangoFilterBackend
from advertisements.permissions import IsAdvertisementOwner
from advertisements.filters import AdvertisementFilter

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter
        

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["update", "delete"]:
            return [IsAuthenticated(), IsAdvertisementOwner()]
        return []
        
