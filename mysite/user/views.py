# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import SignUpForm, EditUserForm
from .models import CustomUser


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, You are signed up successfully')
            return redirect('product:index')
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})


def edit_user(request, user_id):
    user = CustomUser.objects.get(user_id=user_id)
    form = EditUserForm(request.POST or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect('product:index')

    return render(request, 'user/form.html', {'form': form, 'user': user})


@login_required
def profile(request):
    user = CustomUser.objects.get(user_id=request.user.id)

    return render(request, 'user/profile.html', {'user': user})


def users(request):
    users_list = CustomUser.objects.all()

    return render(request, 'user/index.html', {'users_list': users_list})
