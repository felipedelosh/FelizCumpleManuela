"""
Este es el primer codigo que escribo para una ni+a tan linda,
Hola manuela acepte por favor UD mi feliz cumplea+os.
Baby te quiero un monton.

1 - se cargan todas las imagenes.asccii recursos/#nro.txt
las imagenes se hicieron con https://www.ascii-art-generator.org/es.html B&N 120

txt = 120x75


"""

from tkinter import * # Libreria grafica
import tkinter.font as tkFont # Para ajustar el tama+o de las letras
import os # Para saber en que parte del discu duro estan los archivos


class Software:
    def __init__(self):
        self.pantalla = Tk()
        self.tela = Canvas(self.pantalla, width=480, height=720, bg='snow')
        self.fuente = tkFont.Font(family="Lucida Blackletter" ,size=5)
        self.txtManu = Text(self.tela, font=self.fuente, width=120, height=75)
        self.rutaDelProyecto = str(os.path.dirname(os.path.abspath(__file__))) # En donde estoy padado
        self.animaciones = [] # Aka se guarda el texto de la imagen
        self.cargarImagenesAscii()
        self.contadorImg = 0 # La img esta en un vector aca se controla el desplazamiento

        self._configurarPantallaYMostrar()

    def _configurarPantallaYMostrar(self):
        self.pantalla.title("Feliz Cumplea+os Manuelita.")
        self.pantalla.geometry("480x720")
        self.tela.place(x=0, y=0)
        self.txtManu.place(x=0, y=0)
        self.pantalla.after(0, self.refrescarPantalla)
        self.pantalla.mainloop()

    # este metodo refresca la pantalla cada X ms
    def refrescarPantalla(self):
        if self.contadorImg == 50:
            self.contadorImg = 0
        self.ingresarTexto(self.animaciones[self.contadorImg])
        self.contadorImg = self.contadorImg + 1
        
        self.pantalla.after(50, self.refrescarPantalla)

    #Este metodo carga todas las imagenes 
    def cargarImagenesAscii(self):
        """
        Primero se intenta capturar todos los ascii y luego se muestran en el display
        """
        #Capturar
        for i in range(0, 89):
            try:
                ruta = self.rutaDelProyecto + "\\recursos\\" + str(i) + ".txt"
                f = open(ruta, 'r', encoding='UTF-8')
                self.animaciones.append(f.read())
                f.close()
            except:
                pass
            
        
    def ingresarTexto(self, txt):
        self.txtManu.delete(1.0, END)
        self.txtManu.insert(END, txt)

    def mostrarAtributosDeLasImagenes(self):
        """
        Esto solo se usa para vigilar que las imagenes esten cuadradas 
        que esten 
        """
        for i in range(0, 10):
            print('txt: ', i)
            print('Total caracteres: ', len(self.animaciones[i]))
            print('largo: ', len(self.animaciones[i].split('\n')[0]))
            print('Ancho:', len(self.animaciones[i].split('\n')))
            

# SE lanza
HBD = Software()


