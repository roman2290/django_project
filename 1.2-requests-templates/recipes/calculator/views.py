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



context = {
  'recipe': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },

    'recipe': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },

    'recipe': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
  }

def omlet(request):
    servings = request.GET.get('servings')
    if servings:
        context = DATA['omlet']
        for eat in context:
            context[eat] *= int(servings)
        context = {'recipe': context}
    else:
        context = {'recipe': DATA['omlet']}
    return render(request, 'calculator/index.html', context)

def pasta(request):
    servings = request.GET.get('servings')
    if servings:
        context = DATA['pasta']
        for eat in context:
            context[eat] *= int(servings)
        context = {'recipe': context}
    else:
        context = {'recipe': DATA['pasta']}
    return render(request, 'calculator/index.html', context)

def buter(request):
    servings = request.GET.get('servings')
    if servings:
        context = DATA['buter']
        for eat in context:
            context[eat] *= int(servings)
        context = {'recipe': context}
    else:
        context = {'recipe': DATA['buter']}
    return render(request, 'calculator/index.html', context)