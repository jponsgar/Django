from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.nombre}'

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Factura(models.Model):
    nombre = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def subtotal(self):
        return self.cantidad * self.producto.precio

    def __str__(self):
        return f'Factura: {self.id} - Cliente: {self.nombre} - Producto: {self.producto.nombre} - Cantidad: {self.cantidad} - Subtotal: {self.cantidad * self.producto.precio}€'