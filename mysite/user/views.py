# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from .models import User


def users(request):
    user_list = User.objects.all()
    context = {
        'user_list': user_list,
    }
    return render(request, 'user/index.html', context)


def user_detail(request, user_id):
    details = User.objects.get(id=user_id)
    context = {
        'user': details,
    }
    return render(request, 'user/detail.html', context)
