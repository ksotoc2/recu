from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro
from .forms import LibroForm

# Create your views here.
def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/lista_libros.html', {'libros': libros})

def detalle_libro(request):
    libro = get_object_or_404(Libro, id=id)
    return render(request, 'libros/detalle_libro.html', {'libro': libro})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    
    else:
        form = LibroForm()
    return render(request, 'libros/formulario.html', {'form': form})