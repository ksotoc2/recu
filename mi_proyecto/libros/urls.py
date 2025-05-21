from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('libro/', views.detalle_libro, name='detalle_libro'),
    path("nuevo/", views.crear_libro, name='crear_libro' )
]
