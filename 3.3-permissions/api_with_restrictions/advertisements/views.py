from django_filters import DateFromToRangeFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters

from advertisements.models import Advertisement
from advertisements.serializers import AdvertisementSerializer


class CreatePermission(BasePermission):
    message = "У Вас уже открыто десять или более объявлений"

    def has_permission(self, request, view):
        queryset_length = len(Advertisement.objects.filter(creator=request.user.id, status='OPEN'))
        if queryset_length >= 10:
            return False
        return True


class IsOwner(BasePermission):
    message = "Объявление Вам не принадлежит"

    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.creator.id:
            return True
        return False


class AdvFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'description', 'creator',
                  'status', 'created_at']


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = AdvFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated(), CreatePermission()]
        if self.action in ["update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwner()]
        return []
