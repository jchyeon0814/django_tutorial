import random
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dinner(request):
    menus = [{"name":'족발',"price":200}, {"name":'햄버거',"price":400}, {"name":'치킨', "price":800}, {"name":'초밥', "price":1000}]
    pick = random.choice(menus)
    articles = Article.objects.order_by('-pk')

    context = {
        'pick': pick,
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
    
    return redirect('articles:detail', article.pk)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }

    return render(request, 'detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == "POST":
        article.delete()

    return redirect('articles:dinner')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }

    return render(request, 'edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    return redirect('articles:detail', article.pk)