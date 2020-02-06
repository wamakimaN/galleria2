from django.shortcuts import render,reverse,get_object_or_404
from .models import Picture,Category,Location
from django.views import View
from django.views.generic.list import ListView

# Create your views here.
def home_page(request):
  title = 'home'
  categories = Category.all_categs()
  locations = Location.all_locs()
  
  pics = Picture.all_pics()

  return render(request, 'homepage.html', {"title":title,"pics":pics, "categories":categories, "locations":locations})

class PicCategory(ListView):
  model = Picture
  template_name = 'category.html'

  def get_queryset(self):
    self.category = get_object_or_404(Category,pk=self.kwargs['pk'])
    return Picture.objects.filter(category=self.category)

  def get_context_data(self,**kwargs):
    context = super(PicCategory, self).get_context_data(**kwargs)
    context['category'] = self.category
    return context

class PicLocation(ListView):
  model = Picture
  template_name = 'location.html'

  def get_queryset(self):
    self.location = get_object_or_404(Location,pk=self.kwargs['pk'])
    return Picture.objects.filter(location=self.location)

  def get_context_data(self,**kwargs):
    context = super(PicLocation, self).get_context_data(**kwargs)
    context['location'] = self.location
    return context