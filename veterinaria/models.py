from django.db import models
from django.utils import timezone

# Create your models here.
class Persona(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    rol = models.CharField(max_length=11, null=False)
    usuario = models.CharField(max_length=10, null=True)
    contraseña = models.CharField(max_length=10, null=True)

class Mascota(models.Model):
    id = models.AutoField(primary_key=True)
    dueño = models.CharField(max_length=100,null=False,blank=False)
    nombre = models.CharField(max_length=100, null=False)
    cedula = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='cedula_id',null=False)
    edad = models.IntegerField(null=False)
    especie = models.CharField(max_length=100, null=False)
    raza = models.CharField(max_length=100, null=False)
    tamano = models.CharField(max_length=100)
    peso = models.FloatField(null=False)


class Orden(models.Model):
    idOrden = models.AutoField(primary_key=True)
    idMascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, db_column='idMascota',null=False)
    cedulaDueno = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='cedulaDueno',null=False)
    cedulaVeterinarioOrdena = models.CharField(max_length=20)
    nombreMedicamento = models.CharField(max_length=100)
    fecha = models.DateField(default=timezone.now)
    anulacion = models.BooleanField(default=False)

class Factura(models.Model):
    idFactura = models.AutoField(primary_key=True)
    idMascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='facturas_mascota', db_column='idMascota', null=True)
    cedulaDueno = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='facturas_dueno', db_column='cedulaDueno', null=True)
    idorden = models.ForeignKey(Orden, on_delete=models.CASCADE, related_name='facturas_orden', db_column='idOrden', null=True, blank=True)
    producto = models.CharField(max_length=100, null=False)
    cantidad = models.IntegerField(null=False)
    valor = models.FloatField(max_length=100)
    fecha_fact = models.DateField(default=timezone.now)