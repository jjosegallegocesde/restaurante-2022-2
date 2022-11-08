from django.shortcuts import render


#IMPORTAR EL FORMULARIO A RENDER
from web.formularios.formularioPlatos import FormularioPlatos
from web.models import Platos

# Create your views here.
#las vistas en djangp son los CONTROLADORES

#las vistas son funciones de python

def Home(request):
    return render(request,'index.html')


def Menurestaurante(request):

    platosBD=Platos.objects.all()

    data={
        'platos':platosBD
    }

    return render(request,'menurestaurante.html',data)

def PlatosVista(request):

    formulario=FormularioPlatos()
    datosParaTemplate={
        'formularioRegistro':formulario,
        'bandera':False
    }

    #PREGUNTAMOS SI EXISTE ALGUNA PETICION DE TIPO POST ASOCIADA A LA VISTA
    if request.method=='POST':
        #deberiamos capturar los datos del formulario
        datosDelFormulario=FormularioPlatos(request.POST)
        #verificar si los datos llegaron correctamente(VALIDACIONES OK)
        if datosDelFormulario.is_valid():
            #capturamos la data
            datosPlato=datosDelFormulario.cleaned_data
           
            platoNuevo=Platos(
                nombre=datosPlato["nombrePlato"],
                descripcion=datosPlato["descripcionPlato"],
                foto=datosPlato["fotoPlato"],
                precio=datosPlato["precioPlato"],
                tipo=datosPlato["tipoPlato"]
            )

            try:
                platoNuevo.save()
                datosParaTemplate["bandera"]=True
                print("exito")
            
            except Exception as error:
                print(error)



    return render(request,'platos.html',datosParaTemplate)

