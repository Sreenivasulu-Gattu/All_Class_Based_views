from django.shortcuts import render

# Create your views here.

from app.models import *
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

class SchoolList(ListView):
    model = School
    context_object_name = 'schools'

class StudentList(ListView):
    model  = Student
    context_object_name = 'students'

class SchoolDetail(DetailView):
    model = School
    context_object_name = 'schoolobj'

class SchoolCreate(CreateView):
    model = School
    fields = '__all__'

class SchoolUpdate(UpdateView):
    model = School
    fields = '__all__'

class SchoolDelete(DeleteView):
    model = School
    context_object_name = 'school'
    success_url = reverse_lazy('SchoolList')