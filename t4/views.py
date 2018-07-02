from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 't4/index.html')
  
  
def i(request):
    return render(request, 't4/i.html')