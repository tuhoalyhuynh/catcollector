from django.shortcuts import render
from .models import Cat
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

# Cats
def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})

def cats_show(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/show.html', { 'cat': cat })

class CatCreate(CreateView):
    model = Cat
    fields = '__all__'
    success_url = '/cats'

class CatUpdate(UpdateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect('/cats')

class CatDelete(DeleteView):
    model = Cat
    success_url = '/cats'