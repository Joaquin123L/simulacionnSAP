from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.utils.timezone import now
import datetime
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
class Reparacion(models.Model):
    id_reparacion = models.AutoField(primary_key=True)
    id_equipo = models.ForeignKey('Equipo', on_delete=models.CASCADE,db_column='id_equipo')
    motivo = models.CharField(max_length=45)
    fecha_inicio = models.DateField(default=datetime.date.today)
    fecha_fin = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"Reparación {self.id_reparacion} - Motivo: {self.motivo}"

class Estado(models.Model):
    id_estado = models.AutoField(primary_key=True)
    tipo_estado = models.CharField(max_length=45)

    def __str__(self):
        return self.tipo_estado

class TipoEquipo(models.Model):
    id_tipo_equipo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

class Equipo(models.Model):
    id_equipo = models.AutoField(primary_key=True)
    id_estado = models.ForeignKey(Estado, on_delete=models.CASCADE,db_column='id_estado')
    nombre = models.CharField(max_length=45, null=True, blank=True)
    id_tipo_equipo = models.ForeignKey(TipoEquipo, on_delete=models.CASCADE,db_column='id_tipo_equipo')

    def __str__(self):
        return self.nombre or f"Equipo {self.id_equipo}"   