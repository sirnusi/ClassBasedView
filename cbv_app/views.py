from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import School, Student
# Create your views here.

class Home(TemplateView):
    template_name = 'cbv_app/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] =  'BASIC INJECTION'
        return context

class SchoolListView(ListView):
    model = School

class SchoolDetailView(DetailView):
    model = School

class SchoolCreateView(CreateView):
    model = School
    fields = '__all__'
    
class SchoolUpdateView(UpdateView):
    model = School
    fields = ('name', 'principal')
    
class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy('list')