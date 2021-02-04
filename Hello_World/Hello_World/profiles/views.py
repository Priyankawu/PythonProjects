from django.shortcuts import render
from .models import User

# Create your views here.


def admin_console1(request):
    profiles = User.objects.all()   # object is the mgr that interacts with database
    return render(request, "profiles/profiles_page.html", {'profiles': profiles})
