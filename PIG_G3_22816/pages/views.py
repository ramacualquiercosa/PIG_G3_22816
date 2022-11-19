from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Page
from django.urls import reverse_lazy

# Create your views here.
class PageListView(ListView):   
    model = Page

class PageDetailView(DetailView):   
    model = Page


class PageCreate(CreateView):
    model = Page
    fields = ['room', 'name', 'dni', 'entry', 'leave', 'price', 'reserve'] 
    success_url= reverse_lazy ('pages:pages')
