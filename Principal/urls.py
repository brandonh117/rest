from django.conf.urls import url,include
from Principal.views import index
#admin.autodiscover()

urlpatterns = [
    url(r'^$', index),
    
]
 