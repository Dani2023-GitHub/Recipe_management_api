from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from rest_framework import viewsets, permissions, filters
# from django_filters.rest_framework import DjangoFilterBackend
# from .models import Recipe
# from .serializers import RecipeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Recipe, Ingredient, Instruction
from .forms import RecipeForm, IngredientForm, InstructionForm

@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            messages.success(request, 'Recipe created created successfully')
        else:
            messages.error(request, "failed to create recipe")
    
    else:
        form = RecipeForm()
    return render(request, 'recipes/form.html', {
        'title': 'Create recipe',
        'form': form
    })
@login_required
def update_recipe(request, recipe_primary_key):
    recipe = get_object_or_404(Recipe, pk=recipe_primary_key, user = request.user)

    form = RecipeForm(instance=recipe)
    return render(request, 'recipes/form.html', {
        'title': 'Update recipe',
        'form': form,
    })



# class RecipeViewSet(viewsets.ModelViewSet):
#     queryset = Recipe.objects.all()
#     serializer_class = RecipeSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = ['category', 'preparation_time', 'cooking_time', 'servings']
#     search_fields = ['title', 'category', 'ingredients']
#     ordering_fields = ['preparation_time', 'cooking_time', 'servings']

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

#     @action(detail=False, methods =['GET'])
#     def by_ingredient(self, request):
#         ingredient = request.query_params.get('ingredient')
#         if ingredient:
#             recipes = self.queryset.filter(ingrediants__icontains=ingredient)
#             serializer = self.get_serializer(recipes, many=True)
#             return Response(serializer.data)
#         return Response({'Error': 'Ingrediant paraeter is required'}, status=400)

