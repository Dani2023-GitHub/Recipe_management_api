from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
# from rest_framework import viewsets, permissions, filters
# from django_filters.rest_framework import DjangoFilterBackend
# from .models import Recipe
# from .serializers import RecipeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Recipe, Ingredient, Instruction, Category
from .forms import RecipeForm, IngredientForm, InstructionForm

@login_required
def view_recipe(request):
    query = request.GET.get('quey', '')
    category_id = request.GET.get('category', 0)
    recipes = Recipe.objects.all()
    categories = Category.objects.all()

    if category_id:
        recipes = recipes.filter(category_id=category_id)

    if query:
        recipes = recipes.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'recipes/view_recipes.html',{
        'title': "Recipe",
        'recipes': recipes,
        'categories': categories,
    })

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
            print(form.errors)
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

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        form.save()
        messages.success(request, "Recipe updated successfuly")
    else :
        form = RecipeForm(instance=recipe)
        messages.error(request, 'Failed to update')
    return render(request, 'recipes/form.html', {
        'title': 'Update recipe',
        'form': form,
    })

@login_required
def delete_recipe(request, recipe_primary_key):
    recipe = get_object_or_404(Recipe, pk=recipe_primary_key, user = request.user)
    recipe.delete()
    messages.success(request, 'Recipe deleted successfuly')

    return redirect('core_app:home')

@login_required
def create_ingredient(request, recipe_primary_key):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.recipe_id = recipe_primary_key
            ingredient.save()
            messages.success(request, "Ingredient created succesfuly")
        else:
            messages.error(request, "Failed to create ingredient")
    else:
        form = IngredientForm()
    return render(request, 'recipes/form.html', {
        'title': 'create ingredient',
        'form':form
    })

@login_required
def update_ingredient(request, recipe_primary_key, ingredient_primary_key):
    recipe = get_object_or_404(Recipe, pk=recipe_primary_key, user = request.user)
    ingredient = get_object_or_404(Ingredient, pk=ingredient_primary_key, recipe = recipe)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        form.save()
    else:
        form = IngredientForm(instance=ingredient)

    return render(request, 'recipes/form.html', {
        'title': 'update ingredient',
        'form': form
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

