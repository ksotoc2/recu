from django.contrib import admin

# Register your models here.
from .models import Libro, Autor

class AutorAdmin(admin.ModelAdmin):
    list_display = ['user', 'nacionalidad']
    search_fields = ['user__username', 'user__first_name']
    
class  LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'publicado']
    search_fields = ['titulo']
    
admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)