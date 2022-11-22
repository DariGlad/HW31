from rest_framework.viewsets import ModelViewSet

from ads.models import Category
from ads.serializers.category import CategorySerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
