from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.lista_productos, name='productos'),
    path('productos/<int:producto_id>/', views.detalle, name='detalle'),

]
