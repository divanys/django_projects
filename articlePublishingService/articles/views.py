from django.shortcuts import render
from .models import Articles


def articles_home(request):
    articles = Articles.objects.order_by("-date")
    return render(request, "articles/articles_index.html", {"articles": articles})

def create_article(request):
    return render(request, "articles/create_article.html")