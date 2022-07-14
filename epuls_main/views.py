from django.shortcuts import render

# Create your views here.

def homeView(request):
    # nowe zdjęcia 10
    # kluby 4
    return render(request, "epuls_main/home.html",{})