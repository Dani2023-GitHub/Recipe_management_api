from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import RecipeViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

# router = DefaultRouter()
# router.register(r'recipes', RecipeViewSet)
app_name ='recipe'

urlpatterns = [
    path('', views.view_recipe, name='view_recipe' ),
    path('create/', views.create_recipe, name='create_recipe'),
    path('update/<int:recipe_primary_key>/', views.update_recipe, name = 'update_recipe'),
    path('delete/<int:recipe_primary_key>/', views.delete_recipe, name = 'delete_recipe '),
    path('<int:recipe_primary_key>/ingredient/create/', views.create_ingredient, 
         name='create_ingredient'),
    path('<int:recipe_primary_key>/ingredient/update/<int:ingredient_primary_key>/', 
         views.update_ingredient, name='update_ingredient'),
    
#     path('', include(router.urls)),
#     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
