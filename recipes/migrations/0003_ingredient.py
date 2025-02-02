# Generated by Django 5.1.3 on 2025-01-04 13:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_instruction'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=100)),
                ('metric', models.CharField(choices=[('Milligrams', 'Milligrams'), ('Grams', 'Grams'), ('Kilograms', 'Kilograms'), ('Millilitters', 'Millilitters'), ('Litters', 'Litters'), ('Piecies', 'Piecies'), ('Not specified', 'Not specified')], default='Not specified', max_length=20)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe_ingredient', to='recipes.recipe')),
            ],
        ),
    ]
