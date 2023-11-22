
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views import View
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views import View
from core.models import News



def news_record(request):
    News_record = News.objects.all()
    return render(
        request,
        'news.html',
        {
            'News': News_record,
        }
    )





