COLOR_FONDO_PRIMARIO = '#00b8e6'
COLOR_FONDO_SECUNDARIRIO = '#b3dAff'
TITULO_APP = 'APP MOCHI'
COLOR_BOTON = '#008fb3'
#FUNCION QUE NOS PERMITE CENTRAR NUESTRA PANTALLA
def centrar_ventana(objeto, ancho_ventana, largo_ventana):
    pantalla_ancho = objeto.winfo_screenwidth()
    pantalla_largo = objeto.winfo_screenheight()
    x = int((pantalla_ancho/2)-(ancho_ventana/2))
    y = int((pantalla_largo/2)-(largo_ventana/2))
    return objeto.geometry(f'{ancho_ventana}x{largo_ventana}+{x}+{y}')