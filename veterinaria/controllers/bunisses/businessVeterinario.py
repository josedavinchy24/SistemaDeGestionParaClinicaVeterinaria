from model import model
from datetime import date


def RegistrarOrden(veterinaria,idOrden,idmascota,nombreMedicamento,usuario):
    cedulaVeterinario = BuscarVeterinario(veterinaria,usuario)
    ExisteMascotayObtenerCedulaDueno = BuscarMascotayDueno(veterinaria,idmascota)
    ExisteOrdenAnterior = BuscarOrdenSiExiste(veterinaria,idOrden)
    
    if ExisteOrdenAnterior == True:
        print("Ya Existe Orden con ese Id")
        return
    
    if ExisteMascotayObtenerCedulaDueno == False:
        print("La Mascota no esta registrada")
        return
    
    Orden = model.Orden(idOrden,idmascota,ExisteMascotayObtenerCedulaDueno,cedulaVeterinario,nombreMedicamento)
    veterinaria.Ordenes.append(Orden)
    return True
 
def BuscarVeterinario(veterinaria,usuario):
    for datosVeterinario in veterinaria.personas:
        if datosVeterinario.usuario == usuario:
            return datosVeterinario.cedula
    return False

#se tiene que revisar que no deje registrar mascota si no hay dueño registrado
def BuscarMascotayDueno(veterinaria,idmascota):
    for datosMascota in veterinaria.mascotas:
        if datosMascota.idMascota == idmascota:
            return datosMascota.cedulaDueño
    return False

def BuscarOrdenSiExiste(veterinaria,idOrden):
    for orden in veterinaria.Ordenes:
        if orden.idOrden == idOrden:
            return True
    return False

def ImprimirOrden(veterinaria):
    for ordenes in veterinaria.Ordenes:
        print("Orden: "+str(ordenes.idOrden)+", IdMascota: "+str(ordenes.idMascota)+", cedula Dueño: "+ str(ordenes.cedulaDueño) + ", cedula Veterinario: "+str(ordenes.cedulaVeterinarioOrdena)+", nombre Medicamento: "+str(ordenes.nombreMedicamento)+", fecha: "+str(ordenes.fecha))

def ingresarHistoriaYOrden(veterinaria,idMascota,usuario,motivoConsulta,sintomatologia,diagnostico,procedimiento,medicamento,dosisMedicamento,IdOrden,historialVacunacion,medicamentosAlergia,detalleprocedimiento,Anulacion):
    cedulaVeterinario = BuscarVeterinario(veterinaria,usuario)
    if idMascota not in veterinaria.historias:
        veterinaria.historias[idMascota] = {}
    fechaActual = date.today()
    fechaActualString = fechaActual.strftime("%d/%m/%Y")
    registro = {fechaActualString:{"cedulaVeterinario":cedulaVeterinario,"motivoConsulta":motivoConsulta,"sintomatologia":sintomatologia,"diagnostico":diagnostico,"procedimiento":procedimiento,"medicamento":medicamento,"dosisMedicamento":dosisMedicamento,"Orden":IdOrden,"historialVacunacion":historialVacunacion,"medicamentosAlergia":medicamentosAlergia,"detalleprocedimiento":detalleprocedimiento,"Anulacion":Anulacion}}
    veterinaria.historias[idMascota][fechaActualString] = registro[fechaActualString]
    #print(veterinaria.historias)

def AnularOrdenHistoria(veterinaria,IdMascota,IDOrden):
    try:
        for clavePrincipal, valorPrincipal in veterinaria.historias[IdMascota].items():#recorre fechas
            for claveSecundaria, valorSecundario in valorPrincipal.items():#recorre datos
                if IDOrden == valorSecundario and claveSecundaria == 'Orden':
                    veterinaria.historias[IdMascota][clavePrincipal]['Anulacion'] = True
                    #print(veterinaria.historias)
                    return
    except KeyError:
        print("no se pudo realizar la anulacion")
        pass
    

def registrarMascota(veterinaria,nombre,cedulaDueño,edad,especie,raza,tamano,color,peso):
    mascota = model.Mascotas(nombre,cedulaDueño,edad,especie,raza,tamano,color,peso)
    veterinaria.mascotas.append(mascota)
    return True


def imprimirMascotas(veterinaria):
    for mascota in veterinaria.mascotas:
        print("ID Mascota: "+str(mascota.idMascota)+", nombre: "+str(mascota.nombre)+", dueño: "+str(mascota.cedulaDueño))

def imprimirHistoriaClinica(veterinaria,IdMascota):
    try:
        for clavePrincipal, valorPrincipal in veterinaria.historias[IdMascota].items():#recorre fechas
            print("*******************")
            print("FECHA :"+str(clavePrincipal))
            for claveSecundaria, valorSecundario in valorPrincipal.items():#recorre datos
               print(str(claveSecundaria)+": "+str(valorSecundario))
    except KeyError:
        print("no se pudo realizar busqueda")
        pass