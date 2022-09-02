from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display= ["nombre","price","descripcion"]
    list_editable= ["price"]
    search_fields = ["nombre"]

    
admin.site.register(Producto,ProductoAdmin)
