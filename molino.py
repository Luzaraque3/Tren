import random
from tkinter import *

#variables globales
BASE = 460
ALTURA = 220
RADIO = 50

#funcion para modificar arco
def modificar_arco(angulo):
    c.itemconfig(arco, extent=angulo)


ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.geometry("500x500")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="white")

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green", width=480 , height=240 )
frame_graficacion.place(x=10 , y=10)

c = Canvas (ventana_principal , width=BASE, height=ALTURA)
c.config(bg="black")
c.place(x=20,y=20)


"""#triangulo base
polig_1= c.create_polygon(BASE/2,ALTURA/2,BASE,ALTURA,BASE/2,ALTURA,fill="blue")

polig_1= c.create_polygon(BASE/2,ALTURA/2,BASE-120,ALTURA,BASE/2-90,ALTURA,fill="white")

#arcos

arco_1 = c.create_arc(BASE/2-100,ALTURA/2+100,BASE/2+100,ALTURA/2-100, start=90, extent=45, fill="yellow")
arco_2 = c.create_arc(BASE/2-100,ALTURA/2+100,BASE/2+100,ALTURA/2-100, start=180, extent=45, fill="yellow")
arco_3 = c.create_arc(BASE/2-100,ALTURA/2+100,BASE/2+100,ALTURA/2-100, start=270, extent=45, fill="yellow")
arco_4 = c.create_arc(BASE/2-100,ALTURA/2+100,BASE/2+100,ALTURA/2-100, start=360, extent=45, fill="yellow")"""


"""#generar 100 circulos de radio =10, y color y posición aleatoria, sin salirse del canvas
for i in range(30):
    #generar color aleatorio
    color = "#"
    for i in range(6):
        color = color + random.choice("0123456789ABCDEF")
    # generar valor de x e y aleatorio
    radio = random.randint(5,25)
    x = random.randint(0, BASE-2*radio)
    y = random.randint(0,ALTURA-2*radio)
    # circulos
    circulo = c.create_oval(x,y,x+2*radio,y+2*radio, fill=color)

# agregar imagen al canvas
img_nave = PhotoImage(file="img/nave2.png")
nave = c.create_image(BASE/2,ALTURA/2,image=img_nave)

# apa
patma = c.create_arc(BASE/3+50,ALTURA/3-50,BASE/3-50, ALTURA/3+50, start=20, extent=320, fill="yellow")
#punto = c.create_oval(BASE/3-8,ALTURA/3+8,BASE/3+8,ALTURA/3-8, fill="black")"""

# asrco
arco = c.create_arc(BASE/2-RADIO,ALTURA/2-RADIO,BASE/2+RADIO,ALTURA/2+RADIO, start=0,extent=0, fill="blue")

# frame controles
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="green", width=488, height=230)
frame_controles.place(x=10,y=260)

# barra de dezlizamiento
barra_deslizamiento = Scale(frame_controles, label="Angulo", from_=0, to=360, orient="horizontal", length=460, tickinterval=45, command=modificar_arco)
barra_deslizamiento.place(x=10,y=10)

#rectangulo
#rec_1 = c.create_rectangle(BASE/2-100,BASE/2+200,350,ALTURA-20, fill="red")

#desplegar ventana
ventana_principal.mainloop()