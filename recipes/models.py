from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_migrate
from django.dispatch import receiver

class Category(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        #setting plural name
        verbose_name_plural='Categories'

        # order categories by naem
        ordering = ['name',]
    def __str__(self):
        return self.name
CATEGORY_LIST = [
    'Dessert',
    'Main Course',
    'Breakfast', 
    'Vegetarian',
    'Other category'
]

@receiver(post_migrate)
def check_category(sender, **kwargs):
    #check if category table is empty
    if Category.objects.count() == 0:
        for category_name in CATEGORY_LIST:
            category = Category.objects.create(name=category_name)
            category.save()
    
class Recipe(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    preparation_time = models.PositiveIntegerField(help_text='Time in minutes')
    cooking_time = models.PositiveIntegerField(help_text="Time in minutes")
    servings = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    image = models.ImageField(upload_to = 'recipe_images', default='default_recipe_image.png', blank=True, null=True)

    def __str__(self):
        return self.title
    
class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='instructions')
    step_number = models.PositiveIntegerField()
    instruction_text = models.TextField()

    class Meta:
        ordering = ['step_number',]

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=100)
    quantity =models.CharField(max_length=100)

    Milligrams = 'Milligrams'
    Grams='Grams'
    Kilograms='Kilograms'
    Millilitters='Millilitters'
    Litters='Litters'
    Piecies='Piecies'
    Default = 'Not specified'

    METRIC_CHOICE = [
        (Milligrams, 'Milligrams'),
        (Grams, 'Grams'),
        (Kilograms, 'Kilograms'),
        (Millilitters, 'Millilitters'),
        (Litters, 'Litters'),
        (Piecies, 'Piecies'),
        (Default, 'Not specified')

    ]

    metric = models.CharField(max_length=20, choices = METRIC_CHOICE, default=Default)

    def __str__(self):
        return f"{self.quatity} {self.get_metric_display()} of {self.name}"

