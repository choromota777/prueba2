from django.urls import path
from . import views
app_name = 'galeria_espinoza'
urlpatterns = [
 path('listado_galeria/', views.listado_galeria, name='listado_galeria'),
 path('tema1_galeria/', views.tema1_galeria, name='tema1_galeria'),
 path('tema2_galeria/', views.tema2_galeria, name='tema2_galeria'),
]