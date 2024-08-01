from django.shortcuts import render
from rest_framework import generics

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import FoodCategory
from .serializers import FoodListSerializer

class FoodList(generics.ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        categories = FoodCategory.objects.prefetch_related('food__additional').filter(food__is_publish=True).distinct()
        
        # Исключаем категории без опубликованных блюд
        dishes = []
        for category in categories:
            if category.food.filter(is_publish=True).exists():
                dishes.append(category)
        
        return dishes
