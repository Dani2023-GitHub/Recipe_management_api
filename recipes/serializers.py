from rest_framework import serializers
from .models import User, Recipe

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=['id', 'username', 'password', 'email']
#         extra_kwargs = {'password':{'write_only':True}}

# class RecipeSerializer(serializers.ModelSerializer):
#     user=serializers.ReadOnlyField(source='user.username')
#     class Meta:
#         model=Recipe
#         fields=[
#             'id', 'title', 'description', 'ingredients', 'instructions', 'category',
#             'preparation_time', 'cooking_time', 'servings', 'created_date', 'user'
#         ]
