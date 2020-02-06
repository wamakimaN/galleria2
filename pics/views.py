from django.shortcuts import render

# Create your views here.
def home_page(request):
  title = 'home'
  return render(request, 'homepage.html', {"title":title}) 