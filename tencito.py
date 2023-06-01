from tkinter import *

#----------------------
#variables globales
#----------------------
BASE = 660
ALTURA = 560


#------------------------
#ventana principal
#------------------------
ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False, False)
ventana_principal.geometry("700x600")
ventana_principal.config(bg="black")

#--------------------------
#frame de graficas
#--------------------------
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="pink", width=680, height=580)
frame_graficacion.place(x=10, y=10)

#creacion canvas
c = Canvas(frame_graficacion, width=BASE, height=ALTURA)
c.config(bg="coral")
c.place(x=10, y=10)

#dibujaar rectandulo
circu_1 = c.create_oval(BASE/2-210,ALTURA/2-50,BASE/2-140,ALTURA/2+50, fill="red", outline="white")
rect_1 = c.create_rectangle(BASE/2-135,ALTURA/2-65,BASE/2+135,ALTURA/2+65,fill="royalblue",outline="black")
rect_2 = c.create_rectangle(BASE/2-150,ALTURA/2-50,BASE/2-135,ALTURA/2+50,fill="gold", outline="black")
rect_3 = c.create_rectangle(BASE/2-180,ALTURA/2-65,BASE/2-150,ALTURA/2+65,fill="royalblue", outline="black")

# circulos
circu_2 = c.create_oval(BASE/2-120,ALTURA/2+100,BASE/2-50,ALTURA/2+20, fill="darkorange")
rec_4 = c.create_rectangle(BASE/2-70,ALTURA/2+50,BASE/2-10,ALTURA/2+70,fill="black", outline="white")
circu_3 = c.create_oval(BASE/2-30,ALTURA/2+100,BASE/2+40,ALTURA/2+20, fill="darkorange")
rect_5 = c.create_rectangle(BASE/2+70,ALTURA/2+50,BASE/2+10,ALTURA/2+70,fill="black", outline="white")
circu_4 = c.create_oval(BASE/2+60,ALTURA/2+100,BASE/2+130,ALTURA/2+20, fill="darkorange")

#techo
rect_6 = c.create_rectangle(BASE/2-10,ALTURA/2-210,BASE/2+135,ALTURA/2-65,fill="gold", outline="black")
rect_7 = c.create_rectangle(BASE/2+10,ALTURA/2-200,BASE/2+125,ALTURA/2-85,fill="blue", outline="white")
rect_8 = c.create_rectangle(BASE/2-20,ALTURA/2-240,BASE/2+155,ALTURA/2-220,fill="white", outline="white")
#rect_9 = c.create_rectangle(BASE/2-10,ALTURA/2-280,BASE/2+155,ALTURA/2-260,fill="green", outline="white")

#desplegar ventana
ventana_principal.mainloop()