from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomePageView(TemplateView):
    template_name = "core/home.html"
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': "GRUPO 3"})
    
class EjemploPageView(TemplateView):
    template_name = "core/ejemplo.html"

