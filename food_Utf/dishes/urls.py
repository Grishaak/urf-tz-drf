from django.urls import path, include
from rest_framework.routers import DefaultRouter

from dishes.views import FoodApiRetrieveView, FoodCategoryViewList, FoodAllCategoryViewList
from rest_framework import routers

app_name = 'dishes'
# router = routers.DefaultRouter()
# router.register(r'food_category', FoodCategoryViewSet, basename='food_category')

urlpatterns = [
    path('api/v1/foods/', FoodApiRetrieveView.as_view()),
    path(r'api/v1/categories/', FoodCategoryViewList.as_view()),
    path(r'api/v1/all-categories/', FoodAllCategoryViewList.as_view()),
]
