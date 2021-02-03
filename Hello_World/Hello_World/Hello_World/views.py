from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    products = ["Cherries", "Apples", "Oranges", "Strawberries", "Pears", "Watermelons"]
    names = ["Priyanka", "Sanjeev", "Hirsh", "Aaria", "Eshvin"]
    # user = request.user
    context = {'products': products, }
    context1 = {"names": names, }
    # context1 dictionary contains all variables needed in the template.
    return render(request, "home.html", context)  # HttpResponse("<h1>Hello {}!</h1>".format(user))
