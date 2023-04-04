from django.shortcuts import render
from .form import studentform
# Create your views here.
def home(request):
    form=studentform()
    context={
        'form':form
    }
    return render(request,'app/home.html',context)