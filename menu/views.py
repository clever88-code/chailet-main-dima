from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views import View
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views import View
from core.models import Menu


def menu_record(request):
    Menu_record = Menu.objects.all()
    return render(
        request,
        'menu.html',
        {
            'Menu_record': Menu_record,
        }
    )
