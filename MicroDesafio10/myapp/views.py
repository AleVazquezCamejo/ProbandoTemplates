from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
import datetime
from .models import cliente

# Create your views here.


def index(request):
    return HttpResponse("Hola Ale!!")

def mi_formulario(request):
    #return HttpResponse("Hola denuevo!!")
    nombre = "luis"
    apellido = "perez"
    
    diccionario = {"nombre": nombre, "apellido": apellido}
    mi_html = open("myapp/templates/template1.html", "r")
    plantilla = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context(diccionario)
    documento = plantilla.render(mi_contexto)
    return HttpResponse(documento)
    #return render(request, 'myapp\formulario.html')

    
def probandoTemplate(request):
    nombre = "luis"
    apellido = "perez"
    lista_de_notas = [1,2,3,5,8,3,2]
    
    diccionario = {"nombre": nombre, "apellido": apellido, "hoy": datetime.datetime.now(), "notas": lista_de_notas}
    
    plantilla = loader.get_template('template2.html')
    
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)

        
#Este seria para cargar un dato en la base de datos directamente al cargar la pagina

def carga(request):
    cliente1 = cliente(nombre="Alejandro", fecha_nacimiento= "1985-09-17", email= "ale_kosiuk@hotmail.com")
    cliente1.save()
    return HttpResponse("Carga exitosa")


def probando_bootstrap(request):
    # mi_html = open("myapp/templates/index.html", "r")
    # plantilla = Template(mi_html.read())
    # mi_html.close()
    # return HttpResponse(plantilla)
    plantilla = loader.get_template('index.html')
    
    return HttpResponse(plantilla)
    
    #return render (request, 'templates/index.html')
    