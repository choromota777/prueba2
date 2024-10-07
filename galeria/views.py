from django.shortcuts import render

# Create your views here.
def listado_galeria(request):
    return render(request, 'galeria/listado_galeria.html')
def tema1_galeria(request):
    return render(request, 'galeria/tema1_galeria.html')
def tema2_galeria(request):
    return render(request, 'galeria/tema2_galeria.html')