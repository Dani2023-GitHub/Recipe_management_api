from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import RecipeViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

# router = DefaultRouter()
# router.register(r'recipes', RecipeViewSet)
app_name ='recipes'

urlpatterns = [
    path('create/', views.create_recipe, name='create_recipe'),
    path('update/<int:recipe_primary_key>/', views.update_recipe, name = 'update_recipe')
#     path('', include(router.urls)),
#     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
