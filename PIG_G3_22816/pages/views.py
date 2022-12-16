from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Page
from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

# Create your views here.
class PageListView(ListView):   
    model = Page
    
class PageDetailView(DetailView):   
    model = Page

@method_decorator (staff_member_required, name='dispatch')
class PageCreate(CreateView):
    model = Page
    fields = ['room', 'name', 'dni', 'age', 'height', 'weight', 'entry', 'diagnostic', 'medication', 'observation'] 
    success_url= reverse_lazy ('pages:pages')

@method_decorator (staff_member_required, name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    fields = ['room', 'name', 'dni', 'age', 'height', 'weight', 'entry', 'diagnostic', 'medication','observation']
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        return reverse_lazy ('pages:update', args=[self.object.id]) +'?ok'

@method_decorator (staff_member_required, name='dispatch')
class PageDelete(DeleteView):
    model = Page
    success_url= reverse_lazy ('pages:pages')
