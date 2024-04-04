from django.shortcuts import render, redirect
from .models import Store
from .forms import StoreForm, ProductForm

# Create your views here.
def index(request):
    stores = Store.objects.all()
    context = {
        'stores': stores
    }
    return render(request, 'stores/index.html', context)

def detail(request, store_pk):
    store = Store.objects.get(pk=store_pk)
    products = store.product_set.all()
    product_form = ProductForm()
    context = {
        'store': store,
        'products': products,
        'product_form': product_form,
    }
    return render(request, 'stores/detail.html', context)

def create(request):
    if request.method == 'POST':
        store_form = StoreForm(request.POST)
        if store_form.is_valid():
            store = store_form.save()
            return redirect('stores:detail', store.pk)
    else:
        store_form = StoreForm()
    context = {
        'store_form': store_form,
    }
    return render(request, 'stores/create.html', context)

def create_product(request, store_pk):
    store = Store.objects.get(pk=store_pk)
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            product.store = store
            product.user = request.user
            product.save()
    return redirect('stores:detail', store_pk)