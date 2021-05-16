from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Menus
from django.urls import reverse
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
from django import forms

class MenusList(ListView): 
    model = Menus

class MenusCreate(SuccessMessageMixin, CreateView): 
    model = Menus 
    form = Menus
    fields = "__all__" 
    success_message = 'Menu Creado Correctamente !'
 
    def get_success_url(self):        
        return reverse('read')

class MenusDetail(DetailView): 
    model = Menus

class MenusUpdate(SuccessMessageMixin, UpdateView): 
    model = Menus 
    form = Menus 
    fields = "__all__"
    success_message = 'Menus Actualizado Correctamente !'
 
    def get_success_url(self):               
        return reverse('read')

class MenusDelete(SuccessMessageMixin, DeleteView): 
    model = Menus 
    form = Menus
    fields = "__all__"     
 
    def get_success_url(self): 
        success_message = 'Menu Eliminado Correctamente !'
        messages.success (self.request, (success_message))       
        return reverse('read')