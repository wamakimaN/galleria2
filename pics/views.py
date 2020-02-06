from django.shortcuts import render,reverse,get_object_or_404
from .models import Picture,Category,Location
from django.views import View
from django.views.generic.list import ListView

# Create your views here.
def home_page(request):
  title = 'home'
  categories = Category.all_categs()
  
  pics = Picture.all_pics()

  return render(request, 'homepage.html', {"title":title,"pics":pics, "categories":categories})

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