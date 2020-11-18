from django.shortcuts import render
from .models import Item, Keyword, FlowerType, FlowerColor


# Create your views here.

def index(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'posts/index.html', context)

def list_check(request):
    items = Item.objects.all()
    context = {'items': items}

    return render(request, 'posts/list_check.html', context)

def search(request):
    keywords = Keyword.objects.all()
    flowercolors = FlowerColor.objects.all()
    flowertypes = FlowerType.objects.all()
    context = {'keywords': keywords,'flowercolors':flowercolors,'flowertypes':flowertypes }

    return render(request, 'posts/search.html', context)


def search_result(request):
    keyword_op = request.POST.getlist('keyword_op')
    flowercolor_op = request.POST.getlist('flowercolor_op')
    flowertype_op = request.POST.getlist('flowertype_op')

    items = Item.objects.all()

    context = {'items': items, 'keyword_op': keyword_op, 'flowercolor_op': flowercolor_op, 'flowertype_op':flowertype_op}
    return render(request, 'posts/search_result.html', context)

