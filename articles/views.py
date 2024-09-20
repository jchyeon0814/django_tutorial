import random
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dinner(request, name):
    menus = [{"name":'족발',"price":200}, {"name":'햄버거',"price":400}, {"name":'치킨', "price":800}, {"name":'초밥', "price":1000}]
    pick = random.choice(menus)
    articles = Article.objects.order_by('-pk')

    context = {
        'pick': pick,
        'name':name,
        'menus': menus,
        'articles': articles,
    }
    
    return render(request, 'dinner.html', context)

def review(request):
    return render(request, 'review.html')

def create_review(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    article = Article(title=title, content=content)
    article.save() #DB저장 - Article은 모델을 상속받았기 때문에 save는 부모 모델에 정의되어있음
    
    return redirect('/articles/dinner/무언가')