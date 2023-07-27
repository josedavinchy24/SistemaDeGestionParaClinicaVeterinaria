from controller.business import businessVeterinario

def RevisarDatosOrden(veterinaria,idOrden,idmascota,nombreMedicamento,usuario):
    try:
        idOrden = int(idOrden)
    except:
        print("la id Orden debe ser numerico")
        return
    try:
        idmascota = int(idmascota)
    except:
        print("la id Mascota debe ser numerico")
        return
    if nombreMedicamento==None or nombreMedicamento =="":
        print("El nombre del Medicamento no puede estar vacia")
        return
    resultado = businessVeterinario.RegistrarOrden(veterinaria,idOrden,idmascota,nombreMedicamento,usuario)
    return resultado

def ImprimirOrdenes(veterinaria):
    businessVeterinario.ImprimirOrden(veterinaria)

def RevisarHistoriaClinica(veterinaria,idMascota,usuario,motivoConsulta,sintomatologia,diagnostico,procedimiento,medicamento,dosisMedicamento,IdOrden,historialVacunacion,medicamentosAlergia,detalleprocedimiento,Anulacion):
    businessVeterinario.ingresarHistoriaYOrden(veterinaria,idMascota,usuario,motivoConsulta,sintomatologia,diagnostico,procedimiento,medicamento,dosisMedicamento,IdOrden,historialVacunacion,medicamentosAlergia,detalleprocedimiento,Anulacion)


def datosMascota(veterinaria,nombre,cedulaDueño,edad,especie,raza,color,tamano,peso):
    if nombre==None or nombre=="":
        print("El nombre no puede estar vacio")
        return
    try:
        cedulaDueño = int(cedulaDueño)
    except:
        print("la cedula debe ser numerica")
        return
    try:
        edad = int(edad)
    except:
        print("la edad debe ser numerica")
        return
    if especie==None or especie=="":
        print("la especie no puede estar vacia")
        return
    if raza==None or raza=="":
        print("El usuario no puede estar vacio")
        return
    if color==None or color=="":
        print("El color no puede estar vacio")
        return
    if tamano==None or tamano=="":
        print("El usuario no puede estar vacio")
        return
    if peso==None or peso=="":
        print("El usuario no puede estar vacio")
        return
    resultado = businessVeterinario.registrarMascota(veterinaria,nombre,cedulaDueño,edad,especie,raza,tamano,color,peso)
    return resultado




def imprimirMascota(veterinaria):
    businessVeterinario.imprimirMascotas(veterinaria)

def RevisarDatosAnulacion(veterinaria,idmascota,IdOrden):
    businessVeterinario.AnularOrdenHistoria(veterinaria,idmascota,IdOrden)

def RevisarDatosImprimirHistoria(veterinaria,idMascota):
    businessVeterinario.imprimirHistoriaClinica(veterinaria,idMascota)