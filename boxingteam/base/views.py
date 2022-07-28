from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MyUserCreationForm, UserForm


# Create your views here.

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'User name or Password does not exist')

    context = {'page': page}
    return render(request, 'base/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = MyUserCreationForm()

    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    context = {'form': form}
    return render(request, 'base/register-page.html', context)


@login_required(login_url='login')
def updateUser(request):
    form = UserForm(instance=request.user)

    if request.method == "POST":
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated successfully')
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/update-user.html', context)


def index(request):
    users = User.objects.all()

    context = {'users': users}
    return render(request, 'base/index.html', context)


def teamPage(request):
    sections = TypeExercise.objects.all()

    q = request.GET.get('q') if request.GET.get('q') != None else ''

    users = User.objects.filter(section__title__icontains=q)

    context = {'users': users, 'sections': sections}
    return render(request, 'base/team.html', context)


def userPage(request, pk):
    user = User.objects.get(id=pk)

    context = {'user': user}
    return render(request, 'base/profile-page.html', context)
