import tkinter
from tkinter import *
from tkinter import messagebox


val = ""
A = 0
operator = ""

def btn_0_isclicked():
	global val 
	val = val + "0"
	data.set(val)

def btn_1_isclicked():
	global val 
	val = val + "1"
	data.set(val)

def btn_2_isclecked():
	global val
	val = val + "2"
	data.set(val)

def btn_3_isclicked():
	global val 
	val = val + "3"
	data.set(val)

def btn_4_isclicked():
	global val 
	val = val + "4"
	data.set(val)

def btn_5_isclicked():
	global val 
	val = val + "5"
	data.set(val)

def btn_6_isclicked():
	global val 
	val = val + "6"
	data.set(val)

def btn_7_isclicked():
	global val 
	val = val + "7"
	data.set(val)

def btn_8_isclicked():
	global val 
	val = val + "8"
	data.set(val)

def btn_9_isclicked():
	global val 
	val = val + "9"
	data.set(val)

def btn_plus_clicked():
	global A
	global operator
	global val
	A = int(val)
	operator = "+"
	val = val + "+"
	data.set(val)

def btn_subtract_clicked():
	global A
	global operator
	global val
	A = (val)
	operator = "-"
	val = val + "-"
	data.set(val)

def btn_Division_clicked():
	global A
	global operator
	global val
	A = (val)
	operator = "/"
	val = val + "/"
	data.set(val)

def btn_Multiply_clicked():
	global A
	global operator
	global val
	A = int(val)
	operator = "*"
	val = val + "*"
	data.set(val)

def btn_Percentage_clicked():
	global A
	global operator
	global val
	A = (val)
	operator = "%"
	val = val + "%"
	data.set(val)

def btn_point_clicked():
	global A
	global operator
	global val
	A = (val)
	operator = "."
	val = val + "."
	data.set(val)

def c_pressed():
	global A
	global operator
	global val
	val = ""
	A = 0
	operator = ""
	data.set(val)
	

def result():
	global A
	global operator
	global val
	val2 = val
	if operator == "+":
		x = int((val2.split("+")[1]))
		C = A + x
		data.set(C)
		val = str(C)
	elif operator == "-":
		x = int((val2.split("-")[1]))
		C = int(A) - int(x)
		data.set(C)

	elif operator == "*":
		x = int((val2.split("*")[1]))
		c = A * x
		data.set(c)
		val = str(c)

	elif operator == "/":
		x = int((val2.split("/")[1]))
		if x == 0:
			messagebox.showeerror("Error", "Division By 0 Not Supported")
			A = ""
			val = ""
			data.set(val)
		else:
			c = int(A) / int(x)
			data.set(c)
			val = str(c)





root = tkinter.Tk()
root.geometry("250x400+300+300")
root.resizable(0,0)
root.title("Calculator")

data = StringVar()
lbl = Label(
	root,
	text = "Label",
	anchor = SE,
	font = ("Verdana", 20),
	textvariable = data,
	background = "#ffffff",
	fg = "#000000"
)
lbl.pack(expand = True, fill = "both",)

btnrow1 = Frame(root, bg="#000000")
btnrow1.pack(expand = True, fill = "both",)

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both",)

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both",)

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both",)

btnrow5 = Frame(root)
btnrow5.pack(expand = True, fill = "both",)

btnplusminus  = Button(
	btnrow1,
	text = "±",
	font = ("Arial", 18),
	relief = GROOVE,
	border = 0,
)
btnplusminus.pack(side = LEFT, expand = True, fill = "both", )

btnPercentage = Button(
	btnrow1,
	text = "%",
	font = ("Arial", 18),
	relief = GROOVE,
	border = 0,
	command = btn_Percentage_clicked,
)
btnPercentage.pack(side = LEFT, expand = True, fill = "both", )

btnBrackets= Button(
	btnrow1,
	text = "()",
	font = ("Arial", 18),
	relief = GROOVE,
	border = 0,
)
btnBrackets.pack(side = LEFT, expand = True, fill = "both", )


btnreset = Button(
	btnrow1,
	text = "C",
	font = ("Arial", 18),
	relief = GROOVE,
	border = 0,
	command = c_pressed,
		
)
btnreset.pack(side = LEFT, expand = True, fill = "both", )

btn1 = Button(
	btnrow2,
	text = "7",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	command = btn_7_isclicked,
)
btn1.pack(side = LEFT, expand = True, fill = "both", )

btnreset = Button(
	btnrow2,
	text = "8",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	command = btn_8_isclicked,
)
btnreset.pack(side = LEFT, expand = True, fill = "both", )

btndivision = Button(
	btnrow2,
	text = "9",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	command = btn_9_isclicked,
)
btndivision.pack(side = LEFT, expand = True, fill = "both", )
btndivision = Button(
	btnrow2,
	text = "/",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	command = btn_Division_clicked,
)
btndivision.pack(side = LEFT, expand = True, fill = "both", )


btn1 = Button(
	btnrow3,
	text = "4",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	command = btn_4_isclicked,
)
btn1.pack(side = LEFT, expand = True, fill = "both", )

btn2 = Button(
	btnrow3,
	text = "5",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	command = btn_5_isclicked,
)
btn2.pack(side = LEFT, expand = True, fill = "both", )

btn3 = Button(
	btnrow3,
	text = "6",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	command = btn_6_isclicked,
)
btn3.pack(side = LEFT, expand = True, fill = "both", )

btnsubtract= Button(
	btnrow3,
	text = "-",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	command = btn_subtract_clicked,
)
btnsubtract.pack(side = LEFT, expand = True, fill = "both", )

btn1 = Button(
	btnrow4,
	text = "1",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	command = btn_1_isclicked,
)
btn1.pack(side = LEFT, expand = True, fill = "both", )

btn2 = Button(
	btnrow4,
	text = "2",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	command = btn_2_isclecked,
)
btn2.pack(side = LEFT, expand = True, fill = "both", )

btn3 = Button(
	btnrow4,
	text = "3",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	command = btn_3_isclicked,
)
btn3.pack(side = LEFT, expand = True, fill = "both", )

btnmultiply = Button(
	btnrow4,
	text = "*",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	command = btn_Multiply_clicked,
)
btnmultiply.pack(side = LEFT, expand = True, fill = "both", )
 
btnpoint = Button(
	btnrow5,
	text = ".",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	command = btn_point_clicked,
)
btnpoint.pack(side = LEFT, expand = True, fill = "both", )

btn1 = Button(
	btnrow5,
	text = "0",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	command = btn_0_isclicked,
)
btn1.pack(side = LEFT, expand = True, fill = "both", )

btnequal = Button(
	btnrow5,
	text = "=",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	command = result,
)
btnequal.pack(side = LEFT, expand = True, fill = "both", )

btnplus= Button(
	btnrow5,
	text = "+",
	font = ("Verdana", 22),
	relief = GROOVE,
	border = 0,
	command = btn_plus_clicked,
)
btnplus.pack(side = LEFT, expand = True, fill = "both", )
root.mainloop()