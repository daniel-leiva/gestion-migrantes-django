from multiprocessing import context
from re import template
import re
from tkinter.messagebox import NO
from xml.dom.minidom import Identified
from django.shortcuts import render
from django.http import HttpResponse
from appCasaMigrante.models import *
from django.template import loader
from django.contrib import messages



# Create your views here.
def inicio(request):
    template = loader.get_template('inicio.html')

    if request.method == 'GET':
        print("METODO GET")
    
    if request.method == 'POST':
        print("METODO POST")
    
    context = {
        'titulo': "Inicio"
    }
    
    return HttpResponse(template.render(context, request))



def migrantes(request):
    template = loader.get_template('migrantes.html')
    
    if request.method == 'GET':
        id_eliminar = request.GET.get('id_Eliminar', None)
        try:
            RegistroMigrante.objects.filter(pk=id_eliminar).delete()
        except:
            messages.error(request, "Esta información no puede ser eliminada pues está siendo usada en otro modelo")



    if request.method == 'POST':
        nombres = request.POST.get('nombres', None)
        apellidos = request.POST.get('apellidos', None)
        no_identificacion = request.POST.get('no_identificacion', None)
        genero = request.POST.get('genero', None)
        fecha_nacimiento = request.POST.get('fecha_nacimiento', None)
        nacionalidad = request.POST.get('nacionalidad', None)
        fecha_ingreso = request.POST.get('fecha_ingreso', None)
        fecha_salida = request.POST.get('fecha_salida', None)
        comodin = request.POST.get('comodin', None)
        identificador = request.POST.get("identificador", None)


        if comodin == "agregar":
            RegistroMigrante.objects.create(
                nombres = nombres,
                apellidos = apellidos,
                no_identificacion = no_identificacion,
                genero = genero,
                fecha_nacimiento = fecha_nacimiento,
                nacionalidad = nacionalidad,
                fecha_ingreso = fecha_ingreso,
                fecha_salida = fecha_salida,
            )
        
        if comodin == "modificar":
            RegistroMigrante.objects.filter(pk=identificador).update(
                nombres = nombres,
                apellidos = apellidos,
                no_identificacion = no_identificacion,
                genero = genero,
                fecha_nacimiento = fecha_nacimiento,
                nacionalidad = nacionalidad,
                fecha_salida = fecha_salida,
            )


    datos_migrantes = RegistroMigrante.objects.all()

    context = {
        'datos_migrantes': datos_migrantes,
    }
    
    return HttpResponse(template.render(context, request))


def colaboradores(request):
    template = loader.get_template('colaboradores.html')

    if request.method == 'GET':
        id_eliminar = request.GET.get('id_Eliminar', None)
        try:
            RegistroColaborador.objects.filter(pk=id_eliminar).delete()
        except:
            messages.error(request, "Esta información no puede ser eliminada pues está siendo usada en otro modelo")

    if request.method == 'POST':
        nombres = request.POST.get('nombres', None)
        apellidos = request.POST.get('apellidos', None)
        telefono = request.POST.get('telefono', None)
        estado = request.POST.get('estado', None)
        estadoInstancia = EstadoDisponible.objects.get(pk=estado)
        disponibilidad = request.POST.get('disponibilidad',  None)
        disponibilidadInstancia = DiasDisponible.objects.get(pk=disponibilidad)
        comodin = request.POST.get('comodin', None)
        identificador = request.POST.get('identificador', None)

        if comodin == "agregar":
            RegistroColaborador.objects.create(
                nombres = nombres,
                apellidos = apellidos,
                telefono = telefono,
                estado_disponible = estadoInstancia,
                dias_disponible = disponibilidadInstancia,
            )
        
        if comodin  == "modificar":
            RegistroColaborador.objects.filter(pk=identificador).update(
                nombres = nombres,
                apellidos = apellidos,
                telefono = telefono,
                estado_disponible = estadoInstancia,
                dias_disponible = disponibilidadInstancia,
            )
        
    datos_colaboradores = RegistroColaborador.objects.all()
    lista_estados = EstadoDisponible.objects.all()
    lista_diasdisp = DiasDisponible.objects.all()

    context = {
        'datos_colaboradores': datos_colaboradores,
        'lista_estados': lista_estados,
        'lista_diasdisp': lista_diasdisp
    }

    return HttpResponse(template.render(context, request))


def actividades(request):
    template = loader.get_template('actividades.html')

    if request.method == 'GET':
        id_eliminar = request.GET.get('id_Eliminar', None)
        try:
            RegistroActividad.objects.filter(pk=id_eliminar).delete()
        except:
            messages.error(request, "Esta información no puede ser eliminada pues está siendo usada en otro modelo")
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre', None)
        descripcion = request.POST.get('descripcion', None)
        fecha = request.POST.get('fecha', None)
        colab_responsable = request.POST.get('colab_responsable', None)
        colab_respInstancia = RegistroColaborador.objects.get(pk=colab_responsable)
        comodin = request.POST.get('comodin', None)
        identificador = request.POST.get('identificador', None)

        if comodin == "agregar":
            RegistroActividad.objects.create(
                nombre = nombre,
                descripcion = descripcion,
                fecha = fecha,
                colab_responsable = colab_respInstancia,
            )

        if comodin == "modificar":
            RegistroActividad.objects.filter(pk=identificador).update(
                nombre = nombre,
                descripcion = descripcion,
                fecha = fecha,
                colab_responsable = colab_respInstancia,
            )
    
    lista_colaboradores = RegistroColaborador.objects.all()
    datos_actividades = RegistroActividad.objects.all()

    context = {
        'lista_colaboradores': lista_colaboradores,
        'datos_actividades': datos_actividades,
    }

    return HttpResponse(template.render(context, request))

