from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home_page, name='homePage')
]