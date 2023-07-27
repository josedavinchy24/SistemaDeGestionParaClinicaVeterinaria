from model import model
def ingresarUsuaruioCredencial(veterinaria,cedula,nombre,edad,rol, usuario, contrasena):
    persona = model.UsuarioCredenciales(cedula,nombre,edad,rol,usuario,contrasena)
    veterinaria.personas.append(persona)
    return True
#falta ver que no exista otro usuario
def iniciarSesion(veterinaria,usuario,contrasena,rol):
    for sesion in veterinaria.personas:
        if sesion.usuario == usuario and sesion.contrasena == contrasena and sesion.rol == rol:
            return True
    return False

def ingresarDueño(veterinaria,cedula,nombre,edad,rol):
    personassinCredenciales = model.Usuario(cedula,nombre,edad,rol)
    for cedula in veterinaria.personassinCredenciales:
        if cedula.cedula == cedula:
            print("El usuario ya se encuentra registrado")
            return False
    veterinaria.personassinCredenciales.append(personassinCredenciales)
    return True
        


