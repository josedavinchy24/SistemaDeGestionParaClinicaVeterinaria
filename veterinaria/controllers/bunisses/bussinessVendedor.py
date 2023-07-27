from model import model

def ImprimirOrden(veterinaria, id_orden):
    print("hola aca estoy 3")
    for orden in veterinaria.Ordenes:
        if orden.idOrden == id_orden:
            return ("Orden: "+str(orden.idOrden)+", IdMascota: "+str(orden.idMascota)+", cedula Dueño: "+ str(orden.cedulaDueño) + ", cedula Veterinario: "+str(orden.cedulaVeterinarioOrdena)+", nombre Medicamento: "+str(orden.nombreMedicamento)+", fecha: "+str(orden.fecha)) 
        

    print ("no se encontro la orden")        