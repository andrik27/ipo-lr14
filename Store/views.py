from django.shortcuts import render

def home(request):
    return render(request, 'Store/home.html')

def about(request):
    context = {
        'title': 'О магазине',
        'description': 'Магазин игрушек'
    }
    return render(request, 'Store/about.html', context)

def author(request):
    context = {
        'name': 'Крачко Андрей',
        'group': '82ТП',
        'course': '2 Курс'
    }
    return render(request, 'Store/author.html', context)