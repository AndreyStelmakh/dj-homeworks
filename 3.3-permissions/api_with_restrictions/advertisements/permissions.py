from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "Объявление Вам не принадлежит"

    def has_object_permission(self, request, view, obj):
        if request.user.id == obj.creator.id:
            return True
        return False
