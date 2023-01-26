# from rest_framework import serializers
# from .models import Favorites
#
#
# class FavoriteListSerializer(serializers.ModelSerializer):
#     owner_email = serializers.ReadOnlyField(source='owner.email')
#
#     class Meta:
#         model = Favorites
#         fields = ('owner', 'owner_email', 'title', 'price', 'image', 'stock')
#
#
# class FavoriteSerializer(serializers.ModelSerializer):
#     owner_email = serializers.ReadOnlyField(source='owner.email')
#     owner = serializers.ReadOnlyField(source='owner.id')
#
#     class Meta:
#         model = Favorites
#         fields = '__all__'
