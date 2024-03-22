from django.db import models
from datetime import datetime
#from .models import Producto  # Asegúrate de importar el modelo Producto correctamente

# Tu clase Usuarios existente
class Usuarios(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30, null=False)
    apellido = models.CharField(max_length=30, null=False)
    correo= models.CharField(max_length=50, null=False)
    telefono= models.IntegerField(null=False)
    f_nac=models.DateField(null=True)
    f_registro= models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        db_table='usuarios'

class Producto(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0.00)
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2, null=False,default=0.00 )
    stock = models.IntegerField(default=0)

    @property
    def ganancia(self):
        """Calcula la ganancia por producto vendido."""
        return self.precio_venta - self.precio_compra
    @property
    def ganancia_inventario(self):

        return (self.precio_venta - self.precio_compra)* self.stock
        """Calcula la ganancia por producto vendido."""
    

    class Meta:
        db_table = 'productos'

# Clase para manejar las ventas
class Venta(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False)
    fecha_venta = models.DateTimeField(auto_now_add=True)

    pagado = models.BooleanField(default=True)  # Campo nuevo para el estado de pago
    observaciones = models.TextField(blank=True, null=True)  # Campo nuevo para observaciones
    # Si decides agregar un modelo Cliente, aquí iría la relación

    @property
    def total_venta(self):
        return self.cantidad * self.producto.precio_venta
    @property
    def ganancia_venta(self):
        return (self.producto.precio_venta - self.producto.precio_compra) * self.cantidad

    class Meta:
        db_table = 'ventas'


class GastoExtra(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, null=True, blank=True)  # Relación con el modelo Producto
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    observaciones = models.TextField(blank=True, null=True)
    fecha = models.DateTimeField(default=datetime.now)
    descripcion = models.TextField(null=False, blank=True, default=".")

    def __str__(self):
        if self.producto:
            return f"{self.producto.nombre} - {self.cantidad}"
        else:
            # Devolver la descripción si el gasto no está vinculado a un producto
            return f"{self.descripcion} "#- {self.cantidad}"


