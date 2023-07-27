from controller.business import businessUsuarios

# ingresar primer usuarios con credencial
def ingresarusuaruioCredencial(veterinaria,cedula,nombre,edad,rol, usuario, contrasena):
    businessUsuarios.ingresarUsuaruioCredencial(veterinaria,cedula,nombre,edad,rol, usuario, contrasena)


def iniciarSesion(veterinaria,usuario,contrasena,rol):
    if usuario==None or usuario=="":
        print("el usuario no puede ser vacio")
        return
    if contrasena==None or contrasena=="":
        print("la contraseña no puede ser vacio")
        return
    if (usuario != None and usuario != "") and (contrasena != None and contrasena != ""):
        resultado = businessUsuarios.iniciarSesion(veterinaria,usuario,contrasena,rol)
        if resultado == True:
            return resultado
        else:
            print("el usuario o contraseña incorrectos")
            return

# Revisar datos para ingresar un nievo usuario con credecial, se llama la funcion para guardarlo en el 
def datosMedicoVendedor(veterinaria,cedula,nombre,edad,rol,usuario,contrasena):
    try:
        cedula = int(cedula)
    except:
        print("la cedula debe ser numerica")
        return
    if nombre==None or nombre=="":
        print("El nombre no puede estar vacio")
        return
    try:
        edad = int(edad)
    except:
        print("la edad debe ser numerica")
        return
    if usuario==None or usuario=="":
        print("El usuario no puede estar vacio")
        return
    if contrasena==None or contrasena =="":
        print("El contraena no puede estar vacia")
        return
    resultado = businessUsuarios.ingresarUsuaruioCredencial(veterinaria,cedula,nombre,edad,rol,usuario,contrasena)
    return resultado

def datosDueño(veterinaria,cedula,nombre,edad,rol):
    try:
        cedula = int(cedula)
    except:
        print("la cedula debe ser numerica")
        return
    if nombre==None or nombre=="":
        print("El nombre no puede estar vacio")
        return
    try:
        edad = int(edad)
    except:
        print("la edad debe ser numerica")
        return
   
    resultado = businessUsuarios.ingresarDueño(veterinaria,cedula,nombre,edad,rol)
    return resultado

    