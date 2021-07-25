from django.shortcuts import render
from application import models
from django.http import HttpResponseRedirect
from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy
from app import forms
def home(request):
    return render (request,'index.html')
def signup(request):
      if request.method == 'POST':  
        Email = request.POST['Email']
        Passwd = request.POST['Passwd']
        print(Email)
        ins = models.Signup(Email =Email, Passwd=Passwd)
        ins.save()
        return HttpResponseRedirect('apply')

      return render (request,'signup.html')
class applylistview(CreateView):
      model =models.Application
      template_name="application.html"
      fields ='__all__'
      success_url =reverse_lazy('home')
      #form_class ="forms.apply"
      success_url =reverse_lazy('home')


        
    
def about(request):
      return render(request,'about.html')
        