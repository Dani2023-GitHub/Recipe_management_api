from django import forms
from .models import Recipe, Ingredient, Instruction

SELECT_AREA = 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600'
INPUT_CLASSES = 'rounded-r-lg bg-gray-50 border text-gray-900 focus:ring-blue-500 focus:border-blue-500 block flex-1 min-w-0 w-full text-sm border-gray-300 p-2.5  dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
FOR_IMAGE = 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400'
TEXT_AREA = 'block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['category', 'title', 'image', 'preparation_time', 'description', 'cooking_time', 'servings']
        widgets= {
            'category': forms.Select(attrs={
                'class': SELECT_AREA,
                }),
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),

            'image': forms.FileInput(attrs={
                'class': 'FOR_IMAGE'
            }),

            'description': forms.Textarea(attrs={
                'class': TEXT_AREA,
                'placeholder': 'Enter Description...',
                'rows': '4'
            }),

            'preparation_time': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Enter the time it takes to prepare'
            }),

            'cooking_time':forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),

            'servings': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Enter the number of people it can serve'
            })
            
        }

class InstructionForm(forms.ModelForm):
    class Meta:
        model = Instruction
        fields = ['step_number', 'instruction_text']
        widgets = {
            'step_number': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'type': 'number',
                'placeholder': 'Enter step number'
            }),
            'instruction_text': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Enter instruction'
            })
        } 


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'metric']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Enter name'
            }),
            'quantity':forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Enter quantity'
            }),

            'metric': forms.Select(attrs={
                'class': SELECT_AREA
            })

        }
