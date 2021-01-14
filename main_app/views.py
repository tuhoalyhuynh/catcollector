from django.shortcuts import render
from .models import Cat

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})

def cats_show(request, cat_id):
  cat = Cat.objects.get(id=cat_id)
  return render(request, 'cats/show.html', { 'cat': cat })