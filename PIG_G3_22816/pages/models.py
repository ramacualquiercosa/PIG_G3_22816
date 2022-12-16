from django.db import models
from django import forms


class Page(models.Model):
    room = models.SmallIntegerField(verbose_name="Habitación", default=0)
    name =  models.CharField(verbose_name="Nombre y apellido", max_length=200, default="")
    dni =  models.CharField(verbose_name="DNI", max_length=200, default="")
    age = models.CharField(verbose_name="Edad", max_length=200, default="")
    height = models.DecimalField(verbose_name="Altura", max_digits=5, decimal_places=2)
    weight = models.DecimalField(verbose_name="Peso", max_digits=5, decimal_places=2)
    entry = models.DateField(verbose_name="Fecha de ingreso", blank=True, null=True)
    diagnostic = models.CharField(verbose_name="Diagnostico principal", max_length=200, default="")
    medication =  models.CharField(verbose_name="Medicación administrada", max_length=200, default="")
    observation = models.TextField(verbose_name="Observación", max_length=500, null=True, blank=True)
    update = models.DateTimeField(verbose_name="Actualizacion",auto_now=True)
    
    
    

    def resto(self):
        resultado = self.price - self.reserve
        return resultado


    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['name']
     
        



    def __str__(self):
        return self.name
