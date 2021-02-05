from django.http import HttpResponse
from django.shortcuts import render
from profiles.models import User


def home(request):
    products = ["Cherries", "Apples", "Oranges", "Strawberries", "Pears", "Watermelons"]
    names = ["Priyanka", "Sanjeev", "Hirsh", "Aaria", "Eshvin"]
    # user = request.user
    context = {'products': products, }
    profiles = User.objects.all()  # profiles is the database now
    context1 = {"profiles": profiles, }
    # context1 dictionary contains all variables needed in the template.
    # you have to give the database context1 in the render function
    return render(request, "home.html", context1)  # HttpResponse("<h1>Hello {}!</h1>".format(user))
