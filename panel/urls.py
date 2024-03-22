from django.contrib import admin
from django.urls import path

from .views import actualizar_venta

from django import views
from . import views

from .views import exportar_excel
from .views import exportar_excel_ventas
from .views import exportar_excel_gastos

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('listar/', views.listar, name="listar"),
    path('agregar/', views.agregar, name="agregar"),
    path('actualizar/', views.actualizar, name="actualizar"),
    path('eliminar/', views.eliminar, name="eliminar"),

    # Nuevas rutas para productos y ventas siguiendo el estilo solicitado
    path('productos/listar/', views.listar_productos, name='listar_productos'),
    path('productos/agregar/', views.agregar_producto, name='agregar_producto'),
    path('productos/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_producto'),


    path('ventas/registrar/', views.registrar_venta, name='registrar_venta'),
    path('ventas/listar/', views.listar_ventas, name='listar_ventas'),
    path('actualizar_venta/', actualizar_venta, name='actualizar_venta'),
    path('ventas/editar/<int:venta_id>/', views.editar_venta, name='editar_venta'),
    
    
    path('gastos/agregar/', views.registrar_gasto_extra, name='agregar_gasto'),
    path('gastos/listar/', views.listar_gastos_extras, name='listar_gastos_extras'),
    path('gastos/editar/<int:gasto_id>/', views.editar_gasto_extra, name='editar_gasto_extra'),
    path('gastos/eliminar/<int:gasto_id>/', views.eliminar_gasto_extra, name='eliminar_gasto_extra'),

    path('exportar_excel/', exportar_excel, name='exportar_excel'),
    path('exportar_excel_ventas/', exportar_excel_ventas, name='exportar_excel_ventas'),
    path('exportar_excel_gastos/', exportar_excel_gastos, name='exportar_excel_gastos'),

    
]
