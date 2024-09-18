import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dinner(request, name):
    menus = [{"name":'족발',"price":200}, {"name":'햄버거',"price":400}, {"name":'치킨', "price":800}, {"name":'초밥', "price":1000}]
    pick = random.choice(menus)
    context = {
        'pick': pick,
        'name':name,
        'menus': menus,
    }
    return render(request, 'dinner.html', context)

def review(request):
    return render(request, 'review.html')

def create_review(request):
    content = request.POST.get('content')
    print(request.POST)
    context = {
        'content':content,
    }
    return render(request, 'review_result.html', context)