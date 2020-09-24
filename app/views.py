from django.shortcuts import render

# Create your views here.
from app.forms import *

def topic_form(request):
    form=Topic_Form()
    
    if request.method=='POST':
        form_data=Topic_Form(request.POST)
        if form_data.is_valid():
            form_data.save()

    return render(request,'topic_form.html',context={'form':form})


def webpage_form(request):
    form=Webpage_Form()
    if request.method=='POST':
        form_data=Webpage_Form(request.POST)
        if form_data.is_valid():
            form_data.save()
    return render(request,'webpage_form.html',context={'form':form})