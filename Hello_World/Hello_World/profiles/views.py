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


def delete1(request, pk):
    pk = int(pk)
    print(pk)
    item = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('admin_console1')
    content = {"item": item, }
    # I removed "profiles/"from the folowing middle argument. It was causing wrong path. ***
    return render(request, "confirmDelete.html", content)


def confirmed(request):
    if request.method == 'POST':
        #creates from instance and binds data to it
        form = UserForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('admin_console1')
    else:
        return redirect('admin_console1')



def createProfile(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_console1')
    else:
        print(form.errors)
        form = UserForm()
    content = {'form': form}
    return render(request, 'create_profile.html', content)




