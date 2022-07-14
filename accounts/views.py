from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render
from .forms import CreateUserForm

def create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data['password']
            )
            new_user.save()
            login(request, new_user)
            print("Created and Logined")
            return HttpResponse("<h1> Hello </h1>")

    else:
        form = CreateUserForm()
    return render(request, "accounts/register.html", {'form': form})

def login_view(request):
    pass
