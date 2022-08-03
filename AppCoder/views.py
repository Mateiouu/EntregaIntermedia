from django.http import Http404, HttpResponse
from django.shortcuts import render

from .models import *
from .forms import *

# Create your views here.
def inicio(self):
    return render(self, 'inicio.html')





# def atletaFormulario(request):
#     print('method:', request.method)
#     print('post:', request.POST)
   
   
#     if request.method == "POST":
#      miformulario = AtletaFormulario(request.POST)
     
#      if miformulario.is_valid():
        
#         data = miformulario.cleaned_data
        
#         atleta = Atleta(nombre = data['nombre'], apellido = data['apellido'],  nacimiento= data['nacimiento'], diciplina = data['diciplina'], pais = data['pais'])
        
#         atleta.save()
        
#         return render(request, 'inicio.html')
#     else:
#         miformulario = AtletaFormulario()

#     return render(request, "atletas.html", {"miformulario": miformulario})







def atleta(request):
     if request.method =='POST':
           miFormularioA=AtletaFormulario(request.POST)#aquí mellega toda la información del html
           print(miFormularioA)

           if miFormularioA.is_valid:#Si pasó la validación de Django
                 informacion=miFormularioA.cleaned_data
                 atleta=Atleta(nombre=informacion['nombre'],apellido=informacion['apellido'], nacimiento=informacion['nacimiento'], diciplina=informacion['diciplina'], pais=informacion['pais'])
                 atleta.save()
                 return render(request,"inicio.html")#Vuelvo al iniciooadonde quieran
     else:      
           miFormularioA=AtletaFormulario()#Formulario vacio para construir el html
           return render(request,"atletas.html",{"miFormularioA":miFormularioA})


def lista_atletas(self):
   
    lista = Atleta.objects.all()

    return render(self, 'lista_atletas.html', {'lista_atletas': lista})


def busquedaAtleta(request):
    return render(request, 'busquedaAtleta.html')

def buscarAtleta(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        consulta = Atleta.objects.filter(nombre__icontains=nombre)
        return render(request, 'resultadosAtleta.html', {'nombre': nombre, 'consulta': consulta})
          
    else:
            respuesta="No enviaste datos"
      
            return HttpResponse(respuesta)



def entrenador(request):
     if request.method =='POST':
           miFormularioE=EntrenadorFormulario(request.POST)#aquí mellega toda la información del html
           print(miFormularioE)

           if miFormularioE.is_valid:#Si pasó la validación de Django
                informacion=miFormularioE.cleaned_data
                entrenador=Entrenador(nombre=informacion['nombre'],apellido=informacion['apellido'], entrena=informacion['entrena'], email=informacion['email'])
                entrenador.save()
                return render(request,"inicio.html")#Vuelvo al iniciooadonde quieran
     else:      
           miFormularioE=EntrenadorFormulario()#Formulario vacio para construir el html
           return render(request,"entrenadores.html",{"miFormularioE":miFormularioE})

def lista_entrenadores(self):
   
    lista = Entrenador.objects.all()

    return render(self, 'lista_entrenadores.html', {'lista_entrenadores': lista})


def busquedaEntrenador(request):
    return render(request, 'busquedaEntrenador.html')

def buscarEntrenador(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        consulta = Entrenador.objects.filter(nombre__icontains=nombre)
        return render(request, 'resultadosEntrenador.html', {'nombre': nombre, 'consulta': consulta})
          
    else:
            respuesta="No enviaste datos"
      
            return HttpResponse(respuesta)











def deporte(request):
       if request.method =='POST':
           miFormularioD=DeporteFormulario(request.POST)#aquí mellega toda la información del html
           print(miFormularioD)

           if miFormularioD.is_valid:#Si pasó la validación de Django
                informacion=miFormularioD.cleaned_data
                deporte=Deportes(nombre=informacion['nombre'],incluye=informacion['incluye'])
                deporte.save()
                return render(request,"inicio.html")#Vuelvo al iniciooadonde quieran
       else:      
           miFormularioD=DeporteFormulario()#Formulario vacio para construir el html
           return render(request,"deportes.html",{"miFormularioD":miFormularioD})

def lista_deportes(self):
   
    lista = Deportes.objects.all()

    return render(self, 'lista_deportes.html', {'lista_deportes': lista})



def busquedaDeporte(request):
    return render(request, 'busquedaDeporte.html')

def buscarDeporte(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        consulta = Deportes.objects.filter(nombre__icontains=nombre)
        return render(request, 'resultadosDeporte.html', {'nombre': nombre, 'consulta': consulta})
          
    else:
            respuesta="No enviaste datos"
      
            return HttpResponse(respuesta)

