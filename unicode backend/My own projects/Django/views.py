from django.shortcuts import render
from django.http import HttpResponse
from .models import detail
# Create your views here.
def index(request):
 det = detail()   
 det.title = "Go india Give"
 det.about = "Today is the day give it . "
 return render(request,'index.html',{'det':det})
