
from django.shortcuts import render, redirect
from django.http import request, HttpResponse
from .models import *
from datetime import datetime
import requests
from django.contrib import sessions
from django.template import Template, Context
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.http.response import JsonResponse
from proyecto.conexionMongoDB import CRUD
import json
from bson import json_util
from bson import ObjectId
# Create your views here.


def inicio(request):
    return render(request, 'index.html')

def rutaIncorrecta(request):
    return render(request, '404.html')

def home(request):
    return redirect("/home/")


# def IngresarMascota(request):
#     return render(request, 'ingresarMascota.html')


##--------------------------------------vendedor..........,,,,,,,,,,,,,,,,,,,,,,,

def menuVendedor(request):
    usuario = request.session.get('usuario')
    if request.session.get('rol') == "vendedor":
        if request.session.get('usuario'):
            try:
                persona = Persona.objects.get(usuario=usuario, rol="vendedor")
                #INICIO RESTO DE CODIGO


                #FIN CODIGO
                #MUESTRA LA PANTALLA
                return render(request, 'menuVendedor.html', {"vendedor": persona})
            except Persona.DoesNotExist:
                pass
    else:
        return render(request, '404.html')
    return redirect('/login/') 



def menuVeterinario(request):
    usuario = request.session.get('usuario')
    if request.session.get('rol') == "veterinario":
        if request.session.get('usuario'):
            try:
                persona = Persona.objects.get(usuario=usuario, rol="veterinario")
                #INICIO RESTO DE CODIGO


                #FIN CODIGO
                #MUESTRA LA PANTALLA
                return render(request, 'menuVeterinario.html', {"veterinario": persona})
            except Persona.DoesNotExist:
                pass
    else:
        return render(request, '404.html')
    return redirect('/login/') 

def custom_page_not_found(request, not_found):
    return render(request, '404.html', {'not_found': not_found})


# def registarDueno(request):
#     return render(request, 'ingresarDuenoMascota.html')


def historiaClinica(request):
    return render(request, 'IngresarHistoria.html')

##--------------------------------------vendedor..........,,,,,,,,,,,,,,,,,,,,,,,

# def verOrdenes(request):
#     return render(request, 'visualizarOrdenVeterinario.html')


def mostrarListado(request):
    usuario = request.session.get('usuario')
    if request.session.get('rol') == "veterinario":
        if request.session.get('usuario'):
            try:
                persona = Persona.objects.get(usuario=usuario, rol="veterinario")
                #INICIO RESTO DE CODIGO
                pro = Orden.objects.all().values()
                datos = {'pro': pro}
                return render(request, 'visualizarOrdenVeterinario.html', datos)


                #FIN CODIGO
                #MUESTRA LA PANTALLA
                #return render(request, 'menuVeterinario.html', {"veterinario": persona})
            except Persona.DoesNotExist:
                pass
    else:
        return render(request, '404.html')
    return render(request, 'index.html')
    # pro = Orden.objects.all().values()
    # datos = {'pro': pro}
    # return render(request, 'visualizarOrdenVeterinario.html', datos)

def mostrarListadoOrdenVendedor(request):
    usuario = request.session.get('usuario')
    if request.session.get('rol') == "vendedor":
        if request.session.get('usuario'):
            try:
                persona = Persona.objects.get(usuario=usuario, rol="vendedor")
                #INICIO RESTO DE CODIGO


                pro = Orden.objects.all().values()
                datos = {'pro': pro}
                return render(request, 'visualizarOrdenVendedor.html', datos) 

                #FIN CODIGO
                #MUESTRA LA PANTALLA
            except Persona.DoesNotExist:
                pass
    else:
        return render(request, '404.html')
    return redirect('/login/') 

def login_view(request):
    if request.method == 'POST':
        try:
            persona = Persona.objects.get(
                usuario=request.POST['Usuario'], contraseña=request.POST['Password'])
            rol = str((persona.rol).lower())
            request.session['usuario'] = persona.usuario
            request.session['rol'] = rol
            if rol == "veterinario":
                return render(request, 'menuVeterinario.html')

            if rol == "vendedor":
                return render(request, 'menuVendedor.html')
        except Persona.DoesNotExist as e:
            messages.success(request, 'nombre o password incorrecto')
    return render(request, 'login.html')

def logout_view(request):
    request.session.pop('rol', 'na')  # Eliminar la variable 'rol' de la sesión
    return render(request, 'index.html')

def registarDuenoMascota(request):

    usuario = request.session.get('usuario')
    if request.session.get('rol')== "veterinario":
        if request.session.get('usuario'):
            try:
                persona = Persona.objects.get(usuario=usuario, rol="veterinario")
                #INICIO RESTO DE CODIGO
                if request.method == 'POST':
                    nombre = request.POST.get('Name')
                    cedula = request.POST.get('cedula')
                    rol = "usuario"
                    if nombre == None or nombre =="":
                        messages.success(request, "El campo nombre no puede estar vacio")
                        return render(request, 'ingresarDuenoMascota.html')
                    try:
                        persona = Persona.objects.create(
                            nombre=nombre, cedula=cedula, rol=rol)
                        messages.success(request, 'Registro correcto: ' + nombre)
                    except Exception as e:
                        messages.error(request, 'Error al registrar ')
                #FIN CODIGO
                #MUESTRA LA PANTALLA
                return render(request, 'ingresarDuenoMascota.html', {"veterinario": persona})
            except Persona.DoesNotExist:
                pass
    else:
        return render(request, '404.html')
    return render(request, 'index.html')
    # if request.method == 'POST':
    #     nombre = request.POST.get('Name')
    #     cedula = request.POST.get('cedula')
    #     rol = "usuario"

    #     try:
    #         persona = Persona.objects.create(
    #             nombre=nombre, cedula=cedula, rol=rol)
    #         messages.success(request, 'Registro correcto: ' + nombre)
    #     except Exception as e:
    #         messages.error(request, 'Error al registrar ')

    # return render(request, 'ingresarDuenoMascota.html')

def IngresarMascota(request):

    usuario = request.session.get('usuario')
    rol = str(request.session.get('rol').lower())
    if rol == "veterinario":
        if request.session.get('usuario'):
            try:
                persona = Persona.objects.get(usuario=usuario, rol="veterinario")
                #INICIO RESTO DE CODIGO


                if request.method == 'POST':
                    dueño = request.POST.get('Dueño')
                    nombre = request.POST.get('Nombre')
                    cedula_id = request.POST.get('Cedula')
                    edad = request.POST.get('Edad')
                    especie = request.POST.get('Especie')
                    raza = request.POST.get('Raza')
                    tamano = request.POST.get('Tamaño')
                    peso = request.POST.get('Peso')
                # Verifica que el valor de cedula_id no sea nulo
                    if nombre == None or nombre=="":
                        messages.success(request, "El campo nombre no puede estar vacio")
                        return render(request, 'ingresarMascota.html')
                    try:

                        if cedula_id is not None:
                            if (especie !='Gato') and (especie !='Perro') and (especie !='Pez') and (especie !='Ave') :
                                messages.success(request, 'Elija una Especie valida para el registro (Gato, Perro, Ave, Pez)')
                                return render(request, 'ingresarMascota.html')
                            else:
                                try:
                                    # Intenta obtener el objeto Persona correspondiente a cedula_id
                                    persona = Persona.objects.get(cedula=cedula_id)
                                    nombreper = persona.nombre
                                    # Crea la instancia de Mascota con la clave foránea asignada
                                    mascota = Mascota.objects.create(
                                        nombre=nombre, dueño=nombreper, cedula=persona, edad=edad, especie=especie, raza=raza, tamano=tamano, peso=peso)

                                    # Resto del código si es necesario
                                    mascotaid = str(mascota.id)
                                    datos = {
                                        '_id': mascotaid,
                                        'historias': {},
                                    }
                                    CRUD.insert_one(datos)
                                    messages.success(request, 'Registro correcto: ' + nombre)

                                except Persona.DoesNotExist:
                                    # Maneja el caso en que no exista una persona con la cedula_id especificada
                                    messages.success(
                                        request, 'No existe una persona con la cedula especificada para la mascota: ' + nombre)
                        else:
                            # Maneja el caso en que cedula_id es nulo
                            print("El valor de cedula_id es nulo" + cedula_id)
                    except Exception as e:
                        messages.error(request, 'Error al registrar ')


                #FIN CODIGO
                #MUESTRA LA PANTALLA
                return render(request, 'ingresarMascota.html', {"veterinario": persona})
            except Persona.DoesNotExist:
                pass
    else:
        return render(request, '404.html')
    return render(request, 'index.html')



    # if request.method == 'POST':
    #     dueño = request.POST.get('Dueño')
    #     nombre = request.POST.get('Nombre')
    #     cedula_id = request.POST.get('Cedula')
    #     edad = request.POST.get('Edad')
    #     especie = request.POST.get('Especie')
    #     raza = request.POST.get('Raza')
    #     tamano = request.POST.get('Tamaño')
    #     peso = request.POST.get('Peso')
    # # Verifica que el valor de cedula_id no sea nulo

    #     try:

    #         if cedula_id is not None:
    #             if (especie !='Gato') and (especie !='Perro') and (especie !='Pez') and (especie !='Ave') :
    #                 messages.success(request, 'Elija una Especie valida para el registro (Gato, Perro, Ave, Pez)')
    #                 return render(request, 'ingresarMascota.html')
    #             else:
    #                 try:
    #                     # Intenta obtener el objeto Persona correspondiente a cedula_id
    #                     persona = Persona.objects.get(cedula=cedula_id)
    #                     nombreper = persona.nombre
    #                     # Crea la instancia de Mascota con la clave foránea asignada
    #                     mascota = Mascota.objects.create(
    #                         nombre=nombre, dueño=nombreper, cedula=persona, edad=edad, especie=especie, raza=raza, tamano=tamano, peso=peso)

    #                     # Resto del código si es necesario
    #                     mascotaid = str(mascota.id)
    #                     datos = {
    #                         '_id': mascotaid,
    #                         'historias': {},
    #                     }
    #                     CRUD.insert_one(datos)
    #                     messages.success(request, 'Registro correcto: ' + nombre)

    #                 except Persona.DoesNotExist:
    #                     # Maneja el caso en que no exista una persona con la cedula_id especificada
    #                     messages.success(
    #                         request, 'No existe una persona con la cedula especificada para la mascota: ' + nombre)
    #         else:
    #             # Maneja el caso en que cedula_id es nulo
    #             print("El valor de cedula_id es nulo" + cedula_id)
    #     except Exception as e:
    #         messages.error(request, 'Error al registrar ')
    #return render(request, 'ingresarMascota.html')

"""
def post(request):
    if request.method == 'POST':
        medicoVeterinario = request.POST.get('medicoVeterinario')
        motivoDeConsulta = request.POST.get('motivoDeConsulta')
        sintomatologia = request.POST.get('sintomatologia')
        procedimiento = request.POST.get('procedimiento')
        medicamento = request.POST.get('medicamento')
        dosisDeMedicamento = request.POST.get('dosisDeMedicamento')
        medicamentoAlergia = request.POST.get('medicamentoAlergia')
        detalleProcedimiento = request.POST.get('detalleProcedimiento')
        datos = {
            'medicoVeterinario': medicoVeterinario,
            'motivoDeConsulta': motivoDeConsulta,
            'sintomatologia': sintomatologia,
            'procedimiento': procedimiento,
            'medicamento': medicamento,
            'dosisDeMedicamento': dosisDeMedicamento,
            'medicamentoAlergia': medicamentoAlergia,
            'detalleProcedimiento': detalleProcedimiento,
        }
        CRUD.insert_one(datos)
    return render (request,'IngresarHistoria.html')

"""


def post(request):

    usuario = request.session.get('usuario')
    
    if request.session.get('rol') == "veterinario":
        if request.session.get('usuario'):
            try:
                persona = Persona.objects.get(usuario=usuario, rol="veterinario")
                #INICIO RESTO DE CODIGO

                if request.method == 'POST':
                    IDmascota = request.POST.get('IDmascota')
                    medicoVeterinario = request.POST.get('medicoVeterinario')
                    motivoDeConsulta = request.POST.get('motivoDeConsulta')
                    sintomatologia = request.POST.get('sintomatologia')
                    procedimiento = request.POST.get('procedimiento')
                    medicamento = request.POST.get('medicamento')
                    dosisDeMedicamento = request.POST.get('dosisDeMedicamento')
                    medicamentoAlergia = request.POST.get('medicamentoAlergia')
                    detalleProcedimiento = request.POST.get('detalleProcedimiento')
                    fecha_actual = datetime.now().strftime('%Y%m%d%H%M%S')
                    fecha = datetime.now()
                    print(medicamento) 
                    try:
                        if str(medicoVeterinario) == str(persona.cedula):
                                
                                

                            if medicamento:
                                mascota = Mascota.objects.get(id=IDmascota)
                                dueno = Persona.objects.get(cedula=mascota.cedula_id)
                                orden = Orden.objects.create(cedulaDueno=mascota.cedula, idMascota=mascota,
                                                            cedulaVeterinarioOrdena=medicoVeterinario, nombreMedicamento=medicamento, fecha=fecha, anulacion=False)
                                idorden= orden.idOrden
                            else:
                                idorden= 0
                            datos = {
                                fecha_actual: {
                                    'medicoVeterinario': medicoVeterinario,
                                    'motivoDeConsulta': motivoDeConsulta,
                                    'sintomatologia': sintomatologia,
                                    'procedimiento': procedimiento,
                                    'medicamento': medicamento,
                                    'dosisDeMedicamento': dosisDeMedicamento,
                                    'medicamentoAlergia': medicamentoAlergia,
                                    'detalleProcedimiento': detalleProcedimiento,
                                    'Orden': idorden,
                                }}
                        
                            registro = CRUD.find_one({'_id': IDmascota})
                            historias = registro['historias']
                            historias.update(datos)
                            CRUD.update_one({'_id': IDmascota}, {
                                            '$set': {'historias': historias}})
                            messages.success(request, 'Registro exitoso')
                        else:
                            messages.error(request, "Sus cedula no son correctas")

                    except Exception as ex:
                        messages.error(request, str(ex))
                #FIN CODIGO
                #MUESTRA LA PANTALLA
                return render(request, 'IngresarHistoria.html', {"veterinario": persona})
            except Persona.DoesNotExist:
                pass
    else:
        return render(request, '404.html')
    return render(request, 'index.html')


    # if request.method == 'POST':
    #     IDmascota = request.POST.get('IDmascota')
    #     medicoVeterinario = request.POST.get('medicoVeterinario')
    #     motivoDeConsulta = request.POST.get('motivoDeConsulta')
    #     sintomatologia = request.POST.get('sintomatologia')
    #     procedimiento = request.POST.get('procedimiento')
    #     medicamento = request.POST.get('medicamento')
    #     dosisDeMedicamento = request.POST.get('dosisDeMedicamento')
    #     medicamentoAlergia = request.POST.get('medicamentoAlergia')
    #     detalleProcedimiento = request.POST.get('detalleProcedimiento')
    #     fecha_actual = datetime.now().strftime('%Y%m%d%H%M%S')
    #     fecha = datetime.now()
    #     print(medicamento) 
    #     try:
    #         if medicamento:
    #             mascota = Mascota.objects.get(id=IDmascota)
    #             dueno = Persona.objects.get(cedula=mascota.cedula_id)
    #             orden = Orden.objects.create(cedulaDueno=mascota.cedula, idMascota=mascota,
    #                                         cedulaVeterinarioOrdena=medicoVeterinario, nombreMedicamento=medicamento, fecha=fecha, anulacion=False)
    #             idorden= orden.idOrden
    #         else:
    #             idorden= 0
    #         datos = {
    #             fecha_actual: {
    #                 'medicoVeterinario': medicoVeterinario,
    #                 'motivoDeConsulta': motivoDeConsulta,
    #                 'sintomatologia': sintomatologia,
    #                 'procedimiento': procedimiento,
    #                 'medicamento': medicamento,
    #                 'dosisDeMedicamento': dosisDeMedicamento,
    #                 'medicamentoAlergia': medicamentoAlergia,
    #                 'detalleProcedimiento': detalleProcedimiento,
    #                 'Orden': idorden,
    #             }}
        
    #         registro = CRUD.find_one({'_id': IDmascota})
    #         historias = registro['historias']
    #         historias.update(datos)
    #         CRUD.update_one({'_id': IDmascota}, {
    #                         '$set': {'historias': historias}})
    #         messages.success(request, 'Registro exitoso')

    #     except Exception as ex:
    #         messages.error(request, str(ex))
    # return render(request, 'IngresarHistoria.html')


##--------------------------------------vendedor..........,,,,,,,,,,,,,,,,,,,,,,,

def IngresarFactura(request):
    if request.method == 'POST':
        idOrden = request.POST.get('IdOrden')
        producto = request.POST.get('producto')
        cantidad = request.POST.get('cantidad')
        precio = request.POST.get('valor')
        fecha = datetime.now()
        if idOrden == None:
            factura = factura.objects.create(
            idorden=idOrden, producto=producto, cantidad=cantidad, valor=precio, fecha_fact=fecha)
        # else:
        #     try:
        #         #factura = Orden.objects.get(idorden=idOrden)

        #         mascota=Orden.objects.get(id=Orden.idMascota)
        #         cedulaDueno=Persona.objects.get(nombre=Orden.cedulaDueno)
        #         factura = factura.objects.create(
        #         idorden=idOrden, idMascota=mascota,cedulaDueno= cedulaDueno,producto=producto, cantidad=cantidad, valor=precio, fecha_fact=fecha)
        #     except Orden.DoesNotExist:
        #             # Maneja el caso en que no exista una persona con la cedula_id especificada
        #             messages.success(
        #                 request, 'id orden no existe: ' )
    return render(request, 'IngresarFactura.html')


def MostarHistoriaclinica(request):

    usuario = request.session.get('usuario')
    if request.session.get('rol') == "veterinario":
        if request.session.get('usuario'):
            try:
                persona = Persona.objects.get(usuario=usuario, rol="veterinario")
                #INICIO RESTO DE CODIGO


                if request.method == 'POST':
                    IDmascota = request.POST.get('IDhistoria')
                    datos = CRUD.find_one({"_id": IDmascota})
                    return render(request, 'visualizarHistoria.html',{'datos': datos})
                else:
                    historias = CRUD.find()
                    mascotas = {}
                    for historia in historias:
                        mascota_id = historia["_id"]
                        mascota_nombre = Mascota.objects.get(id=mascota_id).nombre
                        
                        if mascota_id not in mascotas:
                            mascotas[mascota_id] = {
                                "idMascota": mascota_id,
                                "nombreMascota": mascota_nombre,
                                "historiasClinicas": []
                            }
                        
                        for fecha, datos in historia["historias"].items():
                            historia_clinica = {
                                "medicoVeterinario": datos["medicoVeterinario"],
                                "motivoDeConsulta": datos["motivoDeConsulta"],
                                "sintomatologia": datos["sintomatologia"],
                                "procedimiento": datos["procedimiento"],
                                "medicamento": datos["medicamento"],
                                "dosisDeMedicamento": datos["dosisDeMedicamento"],
                                "medicamentoAlergia": datos["medicamentoAlergia"],
                                "detalleProcedimiento": datos["detalleProcedimiento"],
                                "fecha": fecha,
                            }
                            mascotas[mascota_id]["historiasClinicas"].append(historia_clinica)



                #FIN CODIGO
                #MUESTRA LA PANTALLA
                return render(request, 'visualizarHistoria.html', {'mascotas': mascotas.values()})
            except Persona.DoesNotExist:
                pass
    else:
        return render(request, '404.html')
    return render(request, 'index.html')

    # if request.method == 'POST':
    #     IDmascota = request.POST.get('IDhistoria')
    #     datos = CRUD.find_one({"_id": IDmascota})
    #     return render(request, 'visualizarHistoria.html',{'datos': datos})
    # else:
    #     historias = CRUD.find()
    #     mascotas = {}
    #     for historia in historias:
    #         mascota_id = historia["_id"]
    #         mascota_nombre = Mascota.objects.get(id=mascota_id).nombre
            
    #         if mascota_id not in mascotas:
    #             mascotas[mascota_id] = {
    #                 "idMascota": mascota_id,
    #                 "nombreMascota": mascota_nombre,
    #                 "historiasClinicas": []
    #             }
            
    #         for fecha, datos in historia["historias"].items():
    #             historia_clinica = {
    #                 "medicoVeterinario": datos["medicoVeterinario"],
    #                 "motivoDeConsulta": datos["motivoDeConsulta"],
    #                 "sintomatologia": datos["sintomatologia"],
    #                 "procedimiento": datos["procedimiento"],
    #                 "medicamento": datos["medicamento"],
    #                 "dosisDeMedicamento": datos["dosisDeMedicamento"],
    #                 "medicamentoAlergia": datos["medicamentoAlergia"],
    #                 "detalleProcedimiento": datos["detalleProcedimiento"],
    #                 "fecha": fecha,
    #             }
    #             mascotas[mascota_id]["historiasClinicas"].append(historia_clinica)

    #     return render(request, 'visualizarHistoria.html', {'mascotas': mascotas.values()})


##--------------------------------------vendedor..........,,,,,,,,,,,,,,,,,,,,,,,
def IngresarFactura(request):

    usuario = request.session.get('usuario')
    if request.session.get('rol') == "vendedor":
        if request.session.get('usuario'):
            try:
                persona = Persona.objects.get(usuario=usuario, rol="vendedor")
                #INICIO RESTO DE CODIGO



                if request.method == 'POST':
                    idOrden_ = request.POST.get('IdOrden')
                    product = request.POST.get('producto')
                    cantidad = request.POST.get('cantidad')
                    precio = request.POST.get('precio')
                    fecha = datetime.now()
                    product2 = str(product.lower())
                    producto= str(product2.strip())
                    try:
                        if idOrden_:
                            pro = Orden.objects.get(idOrden = idOrden_)
                            anulacion = pro.anulacion
                            if pro.nombreMedicamento == producto:
                                if anulacion == False:
                                    url = 'http://localhost:9000/Api/companiesMongo/' 
                                    response = requests.get(url)
                                    if response.status_code == 200:
                                        data = response.json()
                                        companies = data['companies']
                                        for company in companies:
                                            print(company['medicamento'])
                                            if company['medicamento'] == producto:
                        
                                                encontroMedicamento = True
                                                break
                                            else:
                                                encontroMedicamento = False
                                    if encontroMedicamento == True:
                                        try:
                                            _idOrden = Orden.objects.get(idOrden=idOrden_)
                                            factura = Factura.objects.create(
                                                idorden=_idOrden,
                                                idMascota=_idOrden.idMascota,
                                                cedulaDueno=_idOrden.cedulaDueno,
                                                producto=producto,
                                                cantidad=cantidad,
                                                valor=precio,
                                                fecha_fact=fecha
                                                
                                            )
                                            messages.success(request, 'Registro Exitoso')
                                        except Orden.DoesNotExist:
                                            messages.success(request, 'No existe un registro del id ORDEN: ')
                                    else: 
                                        messages.success(request, 'No esta disponible medicamento o no es un medicamento')
                                else:
                                        messages.success(request, 'Orden esta Anulada')
                            else:
                                messages.success(request, 'no es el mismo producto')
                        else:
                            url = 'http://localhost:9000/Api/companiesMongo/' 
                            response = requests.get(url)
                            if response.status_code == 200:
                                data = response.json()
                                companies = data['companies']
                                for company in companies:
                                    print(company['medicamento'])
                                    if company['medicamento'] == producto:
                                        encontroMedicamento = True
                                        break
                                    else:
                                        encontroMedicamento = False
                            if encontroMedicamento == False:
                                factura = Factura.objects.create(
                                    producto=producto,
                                    cantidad=cantidad,
                                    valor=precio,
                                    fecha_fact=fecha

                                )
                                messages.success(request, 'Registro Exitoso')
                            else:
                                messages.success(request, 'no tiene orden para medicamento')
                    except Exception as ex:
                        messages.error(request, str(ex))




                #FIN CODIGO
                #MUESTRA LA PANTALLA
                return render(request, 'IngresarFactura.html', {"vendedor": persona})
            except Persona.DoesNotExist:
                pass
    else:
        return render(request, '404.html')
    return render(request, 'index.html')

    # if request.method == 'POST':
    #     idOrden_ = request.POST.get('IdOrden')
    #     producto = request.POST.get('producto')
    #     cantidad = request.POST.get('cantidad')
    #     precio = request.POST.get('precio')
    #     fecha = datetime.now()

    #     try:
    #         if idOrden_:
    #             pro = Orden.objects.get(idOrden = idOrden_)
    #             anulacion = pro.anulacion
    #             if anulacion == False:
    #                 url = 'http://localhost:9000/Api/companiesMongo/' 
    #                 response = requests.get(url)
    #                 if response.status_code == 200:
    #                     data = response.json()
    #                     companies = data['companies']
    #                     for company in companies:
    #                         print(company['medicamento'])
    #                         if company['medicamento'] == producto:
    #                             encontroMedicamento = True
    #                             break
    #                         else:
    #                             encontroMedicamento = False
    #                 if encontroMedicamento == True:
    #                     try:
    #                         _idOrden = Orden.objects.get(idOrden=idOrden_)
    #                         factura = Factura.objects.create(
    #                             idorden=_idOrden,
    #                             idMascota=_idOrden.idMascota,
    #                             cedulaDueno=_idOrden.cedulaDueno,
    #                             producto=producto,
    #                             cantidad=cantidad,
    #                             valor=precio,
    #                             fecha_fact=fecha
                                
    #                         )
    #                         messages.success(request, 'Registro Exitoso')
    #                     except Orden.DoesNotExist:
    #                         messages.success(request, 'No existe un registro del id ORDEN: ')
    #                 else: 
    #                     messages.success(request, 'No esta disponible medicamento o no es un medicamento')
    #             else:
    #                     messages.success(request, 'Orden esta Anulada')
    #         else:
    #             factura = Factura.objects.create(
    #                 producto=producto,
    #                 cantidad=cantidad,
    #                 valor=precio,
    #                 fecha_fact=fecha

    #             )
    #             messages.success(request, 'Registro Exitoso')
    #     except Exception as ex:
    #         messages.error(request, str(ex))

    # return render(request, 'IngresarFactura.html')


def actualizarOrden(request, id):
        
    usuario = request.session.get('usuario')
    if request.session.get('rol') == "veterinario":
        if request.session.get('usuario'):
            try:
                persona = Persona.objects.get(usuario=usuario, rol="veterinario")
                #INICIO RESTO DE CODIGO
                anulacion = True
                pro = Orden.objects.get(idOrden = id)
                pro.anulacion = anulacion
                pro.save()
                pro = Orden.objects.all().values()
                datos = { 
                    'pro' : pro,
                    'r' : 'Datos Modificados Correctamente!!' 
                }
                return render(request, 'visualizarOrdenVeterinario.html', datos)

                #FIN CODIGO
                #MUESTRA LA PANTALLA
            except Persona.DoesNotExist:
                pass
    else:
        return render(request, '404.html')
    return render(request, 'index.html')

        # anulacion = True
        # pro = Orden.objects.get(idOrden = id)
        # pro.anulacion = anulacion
        # pro.save()
        # pro = Orden.objects.all().values()
        # datos = { 
        #     'pro' : pro,
        #     'r' : 'Datos Modificados Correctamente!!' 
        # }
        # return render(request, 'visualizarOrdenVeterinario.html', datos)

def verMascota(request):
    datos = {}
    if request.method == 'POST':
        try:
            id = request.POST.get('IDmascota')
            mascota = Mascota.objects.get(id=id)
            datos = {'mascota': mascota}
            return render(request, 'visualizarMascotaDueno.html', datos)
        except:     
            return render(request, 'visualizarMascotaDueno.html', datos)
    return render(request, 'visualizarMascotaDueno.html', datos)