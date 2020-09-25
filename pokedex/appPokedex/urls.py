from django.conf.urls import  url
from .views import index,verDetalle

urlpatterns = [
   url(r'^$', index),
   url(r'^detalle/(?P<pokemon_id>\d+)$',verDetalle, name = 'det' ),
    
]