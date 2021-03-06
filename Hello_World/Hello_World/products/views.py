
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

# Create your views here.


def admin_console(request):
    products = Product.objects.all()   # object is the mgr that interacts with database
    return render(request, "products/products_page.html", {'products': products})


def details(request,pk):
    pk = int(pk)
    # item will be the chosen item form the database
    item = get_object_or_404(Product, pk=pk) # red pk is the dictionary object
    #shows all the details of the item chosen
    form = ProductForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('admin_console')
        else:
            print(form.errors)
    else:
        return render(request, 'products/present_product.html', {'form': form})


def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('admin_console')
    content = {"item": item, }
    return render(request, "products/confirmDelete.html", content)

def confirmed(request):
    if request.method == 'POST':
        # creates form instance and binds data to it
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('admin_console') # delete record from the database
    else: # if getting here anywhere else from the delete
        return redirect('admin_console')

def createRecord(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_console')
    else:
        print(form.errors)
        form = ProductForm()
    context = {'form': form, }
    return render(request, 'products/createRecord.html', context)