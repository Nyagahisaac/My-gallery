from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^today/$',views.gallery_of_day,name='galleryToday')
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)