from django.shortcuts import render
from .forms import PostForm
# Create your views here.
def Home(request):
    form=PostForm()
    return render(request,'home.html',{'form':form})