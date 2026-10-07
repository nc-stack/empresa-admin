from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombre_producto = models.CharField(max_length=100, null=True, blank=True)
    cantidad = models.PositiveIntegerField(null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    entregado = models.BooleanField(default=True)

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nombre}"