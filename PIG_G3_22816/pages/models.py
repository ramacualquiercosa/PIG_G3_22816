from django.db import models


class Page(models.Model):
    room = models.SmallIntegerField(verbose_name="Habitación", default=0)
    name =  models.CharField(verbose_name="Nombre y apellido", max_length=200, default="")
    dni =  models.CharField(verbose_name="DNI", max_length=200, default="")
    entry = models.DateField(verbose_name="Fecha de ingreso", blank=True, null=True)
    leave = models.DateField(verbose_name="Fecha de egreso", blank=True, null=True)
    price =  models.IntegerField(verbose_name="Precio por habitación", default=0)
    reserve =  models.IntegerField(verbose_name="Monto abonado", default=0) 
    

    def resto(self):
        resultado = self.price - self.reserve
        return resultado


    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['leave', 'name']

    def __str__(self):
        return self.name
