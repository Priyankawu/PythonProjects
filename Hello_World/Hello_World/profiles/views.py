from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from .forms import UserForm

# Create your views here.


def admin_console1(request):
    profiles = User.objects.all()   # object is the mgr that interacts with database
    return render(request, "home.html", {'profiles': profiles})

# When profiles_detail.html form is submitted, do the following
def details1(request, pk):
    pk = int(pk)
    print("I am in details 1")
    item = get_object_or_404(User, pk=pk)
    form = UserForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('admin_console1')
        else:
            print(form.error)
    else:
        return render(request, "profiles_detail.html", {'form': form})

def delete(request,pk):
    return render(request)

def createProfile(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_console1')
    else:
        print(form.errors)
        form = UserForm()
    context = {'form': form}
    return render(request, 'create_profile.html', context)




