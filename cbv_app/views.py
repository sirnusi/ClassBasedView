from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponse
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
    