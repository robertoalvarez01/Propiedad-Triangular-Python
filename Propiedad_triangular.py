from tkinter import *

#Nucleo de la ejecucion
def ejec():
	try:
		a = float(reca.get())
		b = float(recb.get())
		c = float(recc.get())
		if a+b > c:
			if b+c > a:
				if c+a > b:
					res.set("Si se puede construir")
				else:
					res.set("No se puede construir")
			else:
				res.set("No se puede construir")
		else:
			res.set("No se puede construir")
	except:
		res.set("Debe ingresar valores de tipo numérico")

	vaciar()

#Funcion para vaciar las cajas de texto
def vaciar():
	reca.set("")
	recb.set("")
	recc.set("")
  
#Se definen los colores a utilizar
color = '#%02x%02x%02x' % (230, 230, 230)
letra = '#%02x%02x%02x' % (97, 97, 97)
botonc = '#%02x%02x%02x' % (66, 66, 66)

#Inicio de la ventana
root = Tk()
root.title("Propiedad Triangular (Roberto Alvarez)")
root.iconbitmap('triang.ico')
root.config(bg = color)
root.resizable(0,0)

reca = StringVar()
recb = StringVar()
recc = StringVar()
res = StringVar()

#Titulo
tit = Label(root,text="Bienvenido al programa de Propiedad triangular")
tit.config(font=("Verdana", 20), bg=color, fg=letra)
tit.grid(row=0, column=0, padx=5, pady=5)

#Label correspondiente a recta A
labela = Label(root, text="\nIngrese el valor de la recta A")
labela.config(font=("Verdana", 15), bg=color, fg=letra)
labela.grid(row=1, column=0, padx=5, pady=5)

#Entry correspondiente a la recta A
entrya = Entry(root, textvariable=reca)
entrya.grid(row=2, column=0, padx=5, pady=5)
entrya.config(justify="center", state="normal", font=("Verdana", 14))

#Label correspondiente a recta B
labelb = Label(root, text="\nIngrese el valor de la recta B")
labelb.config(font=("Verdana", 15), bg=color, fg=letra)
labelb.grid(row=3, column=0, padx=5, pady=5)

#Entry correspondiente a la recta B
entrya = Entry(root, textvariable=recb)
entrya.grid(row=4, column=0, padx=5, pady=5)
entrya.config(justify="center", state="normal", font=("Verdana", 14))

#Label correspondiente a recta C
labelb = Label(root, text="\nIngrese el valor de la recta C")
labelb.config(font=("Verdana", 15), bg=color, fg=letra)
labelb.grid(row=5, column=0, padx=5, pady=5)

#Entry correspondiente a la recta C
entrya = Entry(root, textvariable=recc)
entrya.grid(row=6, column=0, padx=5, pady=5)
entrya.config(justify="center", state="normal", font=("Verdana", 14))

#Espacios
esp = Label(root, text="\n")
esp.grid(row=7, column=0, padx=5, pady=5)
esp.config(bg=color)

#Boton accionador
boton = Button(root, text="Consultar", command=ejec)
boton.grid(row=8, column=0, padx=5, pady=5)
boton.config(font=("Verdana", 15), bg=botonc, fg="white")

#Espacios
esp = Label(root, text="\n")
esp.grid(row=9, column=0)
esp.config(bg=color)

#Label de Resultado
resu = Label(root, textvariable=res)
resu.grid(row=10, column=0, padx=5, pady=5)
resu.config(justify="center", state="normal", font=("Verdana", 15), bg=color, fg=letra)

#Espacios
esp = Label(root, text="\n")
esp.grid(row=11, column=0)
esp.config(bg=color)


#Fin Aplicacion
root.mainloop()
