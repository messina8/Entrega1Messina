from django.db import models

# Create your models here.


class Compra(models.Model):
    monto = models.IntegerField()
    recibo = models.BooleanField()
    date = models.DateField(auto_now=True)


class Venta(models.Model):
    monto_efectivo = models.IntegerField(default=0)
    monto_tarjeta = models.IntegerField(default=0)
    monto_mercadopago = models.IntegerField(default=0)
    monto_total = models.IntegerField(auto_created=True, default=monto_efectivo+monto_tarjeta+monto_mercadopago)
    facturado = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)


class Salida(models.Model):
    date = models.DateField(auto_now=True)
    monto = models.IntegerField
    motivo = models.CharField(max_length=25)


class Entrada(models.Model):
    date = models.DateField(auto_now=True)
    monto = models.IntegerField()


class CajaDelDia(models.Model):
    caja_inicial = models.JSONField()
    caja_final = models.JSONField()
    compras = models.JSONField()
    recibos = models.JSONField()
    total_de_ventas_b = models.IntegerField()
    total_de_ventas_n = models.IntegerField()
    salidas = models.JSONField()
    entradas = models.IntegerField()

