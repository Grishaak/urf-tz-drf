from django.db.models import Prefetch, Count, Q
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from dishes.models import Food, FoodCategory
from dishes.serializers import FoodSerializer, FoodListSerializer


class FoodApiRetrieveView(ListCreateAPIView):
    queryset = Food.objects.filter(is_publish=True)
    serializer_class = FoodSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class FoodCategoryViewList(ListCreateAPIView):
    serializer_class = FoodListSerializer

    # Фильтруем все входящие блюда is_publish
    def get_queryset(self):
        queryset = FoodCategory.objects.prefetch_related(
            Prefetch(
                'food',
                queryset=Food.objects.filter(is_publish=True),
                to_attr='filtered_foods'
            )
        ).filter(
            food__is_publish=True
        ).distinct()
        return queryset
