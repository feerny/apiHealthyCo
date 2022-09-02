from django.urls import path,include
from healthyapp import views

urlpatterns = [
    path('',views.Producto_lista),
    path('api/healthyapp',views.Producto_lista),
    path('api/healthyapp/<int:pk>',views.Producto_detalle)
]
