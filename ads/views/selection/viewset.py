from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ads.models import Selection
from ads.permissions import IsOwnerSelection
from ads.serializers import SelectionSerializer, SelectionDetailSerializer, SelectionListSerializer
from users.models import UserRoles


class SelectionViewSet(ModelViewSet):
    queryset = Selection.objects.order_by("name").all()
    default_serializer = SelectionSerializer
    serializer_classes = {
        "retrieve": SelectionDetailSerializer,
        "list": SelectionListSerializer
    }
    default_permission = [AllowAny()]
    permissions = {
        "create": [IsAuthenticated()],
        "destroy": [IsAuthenticated(), IsOwnerSelection()],
        "update": [IsAuthenticated(), IsOwnerSelection()],
        "partial_update": [IsAuthenticated(), IsOwnerSelection()]
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer)

    def create(self, request, *args, **kwargs):
        print(self.permission_classes)
        if request.user.role in (UserRoles.ADMIN, UserRoles.MODERATOR):
            request.data["owner"] = request.data.get("owner", request.user.id)
        else:
            request.data["owner"] = request.user.id

        return super().create(request, *args, **kwargs)
