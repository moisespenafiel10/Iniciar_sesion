from tkinter import *
from config import *
from tkinter import ttk
from funciones import *
class Interfaz_app(Tk):
    def __init__(self):
        super().__init__()#heredamos los métodos
        self.configurar_ventana()
        self.construir_widget()
    #metodo propio vamos a darle las configuraciones basicas para mostrar nuestra ventana
    def configurar_ventana(self):
        self.title(f"{TITULO_APP}")
        self.config(bg=COLOR_FONDO_PRIMARIO)
        self.resizable(0,0)
        self.attributes('-alpha',0.96)
        w,h = 400,250
        centrar_ventana(self,w,h)
    
    def construir_widget(self):
        #cajita de textos
        self.cajas_texto = LabelFrame(self,text='FACEBOOCK',width=150, height=430,bg=COLOR_FONDO_PRIMARIO, fg='white',
        font=('arial',12),relief=FLAT, pady=30)
        self.cajas_texto.grid(column=0, row=0,padx=20, pady=20)
        #caja para capturar el usuario
        self.label_nombre = Label(self.cajas_texto,text='USUARIO', bg=COLOR_FONDO_PRIMARIO, fg='white',font=('Roboto',10)).pack(pady=10)
        self.usuario_texto = Entry(self.cajas_texto,bd=0, width=12, font=('arial',12))
        self.usuario_texto.focus()
        self.usuario_texto.pack()
        #caja para capturar contraseña
        self.label_password= Label(self.cajas_texto,text='CONTRASEÑA', bg=COLOR_FONDO_PRIMARIO, fg='white',font=('Roboto',10)).pack(pady=10)
        self.password_texto = Entry(self.cajas_texto,bd=0, width=12, font=('Roboto',12))
        self.password_texto.pack()
        #cajita de botones
        self.cajas_botones = LabelFrame(self,width=150, height=430,bg=COLOR_FONDO_PRIMARIO, fg='white',
        font=('arial',12),relief=FLAT, pady=60)
        self.cajas_botones.grid(column=1, row=0,padx=20, pady=20)
        # #boton nuevo
        self.nuevo = Button(self.cajas_botones, text='Registrarse',command=lambda:nuevo(self), bg=COLOR_BOTON, fg='white', relief=FLAT, bd=0,
        width=20, height=2, font=('Arial',10)).pack(pady=8)
        #boton de iniciar sesion

        self.actualizar = Button(self.cajas_botones, text='inisiar sesion ',command=lambda:iniciar_sesion(self), bg=COLOR_BOTON, fg='white', relief=FLAT,
        bd=0, width=20, height=2, font=('Arial',10)).pack(pady=8)
        # #boton de eliminar
        # self.eliminar = Button(self.cajas_botones, text='eliminar',command=lambda:eliminar(self), bg=COLOR_BOTON, fg='white', relief=FLAT,
        # bd=0, width=20, height=2, font=('Arial',10)).pack(pady=8)
        # #boton de cancelar
        # self.cancelar = Button(self.cajas_botones, text='cancelar',command=lambda:limpiar(self), bg=COLOR_BOTON, fg='white', relief=FLAT, bd=0, width=20,
        # height=2, font=('Arial',10)).pack(pady=8)
        # #fin de cajitas de botones

        # #tabla de datos
        # self.cajas_datos = LabelFrame(self,text='cajas de texto',width=600, height=360,bg=COLOR_FONDO_PRIMARIO, fg='white',
        # font=('arial',12),relief=FLAT, pady=60)
        # self.cajas_datos.grid(column=2, row=0,padx=20, pady=20)
        # #tabla
        # self.tabla_datos = ttk.Treeview(self.cajas_datos, columns=('#1','#2','#3'))
        # self.tabla_datos.column('#0',width=40)
        # self.tabla_datos.column('#1',width=40)
        # self.tabla_datos.column('#02',width=120)
        # self.tabla_datos.column('#03',width=40)
        # self.tabla_datos.heading('#0',text='id')
        # self.tabla_datos.heading('#1',text='Nombre')
        # self.tabla_datos.heading('#2',text='Apellido')
        # self.tabla_datos.heading('#3',text='Celular')
        # alumnitos = db.mostrar('Usuarios')
        # for id,nom,ape,num in alumnitos:
        #     self.tabla_datos.insert('',END,text=id, values=(nom,ape,num))
        # self.tabla_datos.place(x=0, y=0, width=400,height=600)
        # # self.tabla_datos.insert('', END, text='hola', values=('rodriguez','93344'))
        # self.tabla_datos.bind('<Double-1>',lambda event:doble_clic(self,event))
        # #fin de tabla de datos