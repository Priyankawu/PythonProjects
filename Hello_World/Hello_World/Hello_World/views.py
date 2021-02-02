from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # products = ["Cherries", "Apples", "Oranges", "Strawberries", "Pears", "Watermelons"]
    names = ["Priyanka", "Sanjeev", "Hirsh", "Aaria", "Eshvin"]
    # user = request.user
    # context = {'products': products, }
    context1 = {"names": names, }
    return render(request, "home.html", context1)  # HttpResponse("<h1>Hello {}!</h1>".format(user))
