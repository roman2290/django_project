from django.shortcuts import render
from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


# Роман, добрый день.
# Спасибо за работу.
# - Использование шаблона для отображения данных: Вы корректно используете функцию render для передачи контекста в шаблон, что упрощает работу с отображением данных на веб-странице.
# - Обработка количества порций: Вы предусмотрели обработку параметра servings, что позволяет пользователям настраивать количество ингредиентов в зависимости от количества порций.

# Рекомендации
# Избавьтесь от дублирования кода:

# В настоящее время функции omlet, pasta и buter содержат много повторяющегося кода. Вы можете создать одну универсальную функцию для обработки всех запросов, передавая название рецепта в качестве аргумента.
# Улучшите обработку параметра servings:

# В текущей реализации нет проверки на то, является ли параметр servings числом и больше ли оно нуля. Добавьте эту проверку, чтобы избежать возможных ошибок.
# Исправьте ошибку в коде:

# Переменная context определена несколько раз в одном и том же пространстве имен, что приведет к тому, что последние данные будут затирать предыдущие. Это нужно исправить.
# Пример

def get_recipe(request, dishname):
    servings = request.GET.get('servings', 1)
    try:
        servings = int(servings)
        if servings <= 0:
            servings = 1
    except ValueError:
        servings = 1

        recipe = DATA.get(dishname, {}).copy()
    for ingredient, amount in recipe.items():
        recipe[ingredient] = amount * servings

    context = {'recipe': recipe}
    return render(request, 'calculator/index.html', context)

def omlet(request):
    return get_recipe(request, 'omlet')

def pasta(request):
    return get_recipe(request, 'pasta')

def buter(request):
    return get_recipe(request, 'buter')

# context = {
#   'recipe': {
#         'яйца, шт': 2,
#         'молоко, л': 0.1,
#         'соль, ч.л.': 0.5,
#     },

#     'recipe': {
#         'макароны, г': 0.3,
#         'сыр, г': 0.05,
#     },

#     'recipe': {
#         'хлеб, ломтик': 1,
#         'колбаса, ломтик': 1,
#         'сыр, ломтик': 1,
#         'помидор, ломтик': 1,
#     },
#   }

# def omlet(request):
#     servings = request.GET.get('servings')
#     if servings:
#         context = DATA['omlet']
#         for eat in context:
#             context[eat] *= int(servings)
#         context = {'recipe': context}
#     else:
#         context = {'recipe': DATA['omlet']}
#     return render(request, 'calculator/index.html', context)

# def pasta(request):
#     servings = request.GET.get('servings')
#     if servings:
#         context = DATA['pasta']
#         for eat in context:
#             context[eat] *= int(servings)
#         context = {'recipe': context}
#     else:
#         context = {'recipe': DATA['pasta']}
#     return render(request, 'calculator/index.html', context)

# def buter(request):
#     servings = request.GET.get('servings')
#     if servings:
#         context = DATA['buter']
#         for eat in context:
#             context[eat] *= int(servings)
#         context = {'recipe': context}
#     else:
#         context = {'recipe': DATA['buter']}
#     return render(request, 'calculator/index.html', context)