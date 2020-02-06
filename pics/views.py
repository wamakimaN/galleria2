from django.shortcuts import render
from .models import Picture,Category,Location

# Create your views here.
def home_page(request):
  title = 'home'
  
  pics = Picture.all_pics()

  return render(request, 'homepage.html', {"title":title,"pics":pics})