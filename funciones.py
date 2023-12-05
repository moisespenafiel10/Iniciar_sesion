from tkinter import *
from tkinter.messagebox import *
import orm
from Tablas.Usuarios import Usuarios
db=orm.SQLiteORM("mi_base_de_datos")
#creamos nuestra base de datos
db.crear_tabla(Usuarios)   
def limpiar(ventana):
    ventana.usuario_texto.delete(0,END)
    ventana.password_texto.delete(0,END)
    # ventana.ususario_texto.focus() 
def nuevo(ventana):
    name = ventana.usuario_texto.get()
    password = ventana.password_texto.get()
    
    date = {
        "usuario":name,
        "password":password,
    }
    db.insertarUno('Usuarios',date)
    showinfo(title='save', message='registrado')
    # #nuevo
    # id = db.mostrar('Usuarios', where=f'password={password}')[0][0]
    # ventana.tabla_datos.insert('',END, text=id, values=(name,password))
    # limpiar(ventana)

def iniciar_sesion(ventana):
    usuario = ventana.usuario_texto.get()
    contraseña = ventana.password_texto.get()

    # Verificar si el usuario y la contraseña coinciden con los datos en la base de datos
    usuario_encontrado = db.mostrar('Usuarios', where=f"usuario='{usuario}' AND password='{contraseña}'")
    
    if usuario_encontrado:
        usuario = usuario_encontrado[0][0]  # Suponiendo que el primer valor en la fila es el ID de usuario
        nombre_usuario = usuario_encontrado[0][1]  # Suponiendo que el segundo valor es el nombre de usuario
        
        # Aquí podrías realizar acciones posteriores al inicio de sesión exitoso
        # Por ejemplo, mostrar un mensaje de bienvenida o cargar otra ventana
        showinfo(title='Inicio de sesión exitoso', message=f'Bienvenido, {nombre_usuario}!')
        # Realiza las operaciones necesarias después de un inicio de sesión exitoso

        # Limpia los campos de texto después de un inicio de sesión exitoso
        limpiar(ventana)
        
        # Aquí podrías continuar con la lógica de tu aplicación después del inicio de sesión exitoso
        # Por ejemplo, cambiar a otra ventana o realizar alguna otra acción
    else:
        showerror(title='Error de inicio de sesión', message='Nombre de usuario o contraseña incorrectos.')

# Uso de la función de inicio de sesión desde la interfaz gráfica (suponiendo que se llama al presionar un botón "Iniciar Sesión")
# Puedes conectar esta función a un evento en tu interfaz gráfica (por ejemplo, un botón "Iniciar Sesión") para que se ejecute cuando se active dicho evento
# iniciar_sesion(ventana)


           
