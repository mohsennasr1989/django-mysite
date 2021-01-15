# Create your views here.
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import UserForm, SignUpForm
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


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, You are signed up successfully')
            return redirect('user:index')
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})
