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
    custom_user = CustomUser.objects.get(user_id=user_id)
    form = EditUserForm(request.POST or None, instance=custom_user)

    if form.is_valid():
        form.save()
        return redirect('product:index')

    return render(request, 'user/form.html', {'form': form, 'custom_user': custom_user})


@login_required
def profile(request):
    custom_user = CustomUser.objects.get(user_id=request.user.id)

    return render(request, 'user/profile.html', {'custom_user': custom_user})


@login_required
def users(request):
    if request.user.is_superuser:
        users_list = CustomUser.objects.all()
        return render(request, 'user/index.html', {'users_list': users_list.order_by('id')})
    else:
        return redirect('profile')


def remove_user(request, user_id):
    user = CustomUser.objects.get(user_id=user_id)

    if request.method == 'POST':
        user.delete()
        return redirect('user:index')

    return render(request, 'user/remove_confirm.html', {'user': user})
