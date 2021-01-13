# Create your views here.
from django.shortcuts import render, redirect

from .forms import UserForm
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


def add_user(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('user:index')
