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

    return render(request, 'user/form.html', {'form': form})


def edit_user(request, user_id):
    user = User.objects.get(id=user_id)
    form = UserForm(request.POST or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect('user:index')

    return render(request, 'user/form.html', {'form': form, 'user': user})


def remove_user(request, user_id):
    user = User.objects.get(id=user_id)

    if request.method == 'POST':
        user.delete()
        return redirect('user:index')

    return render(request, 'user/remove_confirm.html', {'user': user})
