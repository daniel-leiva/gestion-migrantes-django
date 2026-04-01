from urllib import request
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class RegistroMigrante(models.Model):
    #Modelo para el registro de los Migrantes

    nombres = models.CharField(max_length=30, null=False, blank=False)
    apellidos = models.CharField(max_length=30, null=False, blank=False)
    no_identificacion = models.CharField(max_length=30, null=False, blank=False)
    genero = models.CharField(max_length=10, null=False, blank=False)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    nacionalidad = models.CharField(max_length=20, null=False, blank=False)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_salida = models.DateTimeField(null=False, blank=False,)

    class Meta:
        #Nombre de la tabla en base de datos
        db_table = 'Migrantes'
        verbose_name_plural = 'Registro de los Migrantes'
    
    def __str__(self):
        return str(self.nombres) + str(self.apellidos)


class EstadoDisponible(models.Model):
    #Modelo para registrar los estados de disponibilidad

    estado_disponible = models.CharField(max_length=20, null=False, blank=False)

    class Meta:
        db_table = 'EstadoDisponibilidad'
        verbose_name_plural = 'Estados de Disponibilidad'
    
    def __str__(self):
        return str(self.estado_disponible)


class DiasDisponible(models.Model):
    #Modelo para registrar los días de disponibilidad

    dias_disponible = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        db_table = 'DiasDisponibilidad'
        verbose_name_plural = 'Días de Disponibilidad'
    
    def __str__(self):
        return str(self.dias_disponible)


class RegistroColaborador(models.Model):
    #Modelo para el registro de los Colaboradores

    nombres = models.CharField(max_length=30, null=False, blank=False)
    apellidos = models.CharField(max_length=30, null=False, blank=False)
    telefono = models.IntegerField(null=False, blank=False)
    estado_disponible = models.ForeignKey(EstadoDisponible, on_delete=models.PROTECT, default=1)
    dias_disponible = models.ForeignKey(DiasDisponible, on_delete=models.PROTECT, default=1)

    class Meta:
        #Nombre de la tabla en base de datos
        db_table = 'Colaboradores'
        verbose_name_plural = 'Registro de Colaboradores'

    def __str__(self):
        return str(self.nombres)+ " " + str(self.apellidos)


class RegistroActividad(models.Model):
    #Modelo para el registro de las Actividades
    nombre = models.CharField(max_length=20, null=False, blank=False)
    descripcion = models.CharField(max_length=100, null=False, blank=False)
    fecha = models.DateTimeField(null=False, blank=False)
    colab_responsable = models.ForeignKey(RegistroColaborador, on_delete=models.PROTECT)

    class Meta:
        #Nombre de la table en base de datosfff
        db_table = 'Actividades'
        verbose_name_plural = 'Registro de Actividades'

    def __str__(self):
        return str(self.nombre)


