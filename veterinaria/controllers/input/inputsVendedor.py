
from controller.business import businessVeterinario
from controller.business import bussinessVendedor

def RevisarVentaidOrden(veterinaria,idOrden):
    try:
        idOrden = int(idOrden)
    except:
        print("la id Orden debe ser numerico")
        return 
    
    if idOrden==None or idOrden =="":
        print("El campo id no puede estar vacia")
        return
    
    resultado = businessVeterinario.BuscarOrdenSiExiste(veterinaria, idOrden)
    return resultado


def imprimirordenventa(veterinaria, id_orden):
    print("hola aca estoy 2")
    bussinessVendedor.ImprimirOrden (veterinaria, id_orden)





