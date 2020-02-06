from django.conf.urls import url
from django.conf import settings
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home_page, name='homePage'),
    url(r'^category/(?P<pk>[\d]+)/$',views.PicCategory.as_view(),name='view_by_category')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
