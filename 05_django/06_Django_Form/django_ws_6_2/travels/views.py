from django.shortcuts import render
from .models import Travels
from .forms import TravelsForm

# Create your views here.
def index(request):
    travels = Travels.objects.all()
    context = {
        'travels': travels,
    }
    return render(request, 'travels/index.html', context)

def create(request):
    form = TravelsForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            travel = form.save()
            context = {
                'travel': travel,
            }
            return render(request, 'travels/detail.html', context)
    else:
        form = TravelsForm()
    context = {
        'form': form,
    }
    return render(request, 'travels/create.html', context)

def detail(request, pk):
    travel = Travels.objects.get(pk=pk)
    context = {
        'travel': travel,
    }
    return render(request, 'travels/detail.html', context)