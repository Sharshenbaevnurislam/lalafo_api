# from django.shortcuts import render
# from rest_framework import generics, permissions
# from rest_framework.viewsets import ModelViewSet
#
# from product.permissions import IsAuthor
# from .models import Product
# from . import serializers
#
#
# class FavoriteViewSet(ModelViewSet):
#     # queryset = Product.objects.all()
#     #
#     # def perform_create(self, serializer):
#     #     serializer.save(owner=self.request.user)
#     #
#     # def get_serializer_class(self):
#     #     if self.action == 'list':
#     #         return serializers.FavoriteListSerializer
#     #     return serializers.FavoriteSerializer
#     #
#     # def get_permissions(self):
#     #     if self.action in ('update', 'partial_update', 'destroy'):
#     #         return [permissions.IsAuthenticated(), IsAuthor()]
#     #     return [permissions.IsAuthenticatedOrReadOnly()]
