# import the necessary packages
from timeit import timeit
from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import time
import cv2
import os

panelA = None
panelB = None
initiated = False
loading_label: Label = None
result_label: Label = None
bg_color = '#EBEBEB'
title_size = 75

def process_show(path_input):
	global loading_label
	image = cv2.imread(path_input)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)	
	output = cv2.Canny(gray, 50, 100)
	cv2.imwrite('output_0.png', output)

	print('loading...')
	start_time = time.time()
	time.sleep(3)
	end_time = time.time()

	loading_label.configure({'text': f'{round(end_time-start_time, 4)} seconds'})
	result_label.configure({'text': f'Result: Image after canny'})
	show_images(path_input, 'output_0.png')
	

def show_images(path_input, path_output='output.png'):
	# grab a reference to the image panels
	global panelA, panelB, initiated
	# open a file chooser dialog and allow the user to select an input
	# image
	print('image path: ', path_input); 
	print('file is valid: ', os.path.isfile(path_input))
	if len(path_input) > 0:
		# load the image from disk, convert it to grayscale, and detect
		# edges in it
		image = cv2.imread(path_input)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		if path_output=="":
			output = cv2.Canny(gray, 50, 100)
		else:
			output = cv2.imread(path_output)
			output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)

		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		
		image = Image.fromarray(image)
		output = Image.fromarray(output)
		image = image.resize([400, 400])
		output = output.resize([400, 400])

		image = ImageTk.PhotoImage((image))
		output = ImageTk.PhotoImage(output)

		if not initiated:
			panelA = Label(image=image, bg=bg_color)
			panelA.image = image
			panelA.pack(side="left")
			panelA.place(x=75, y=title_size+50)

			panelB = Label(image=output, bg=bg_color)
			panelB.image = output
			panelB.pack(side="right")
			panelB.place(x=681, y=title_size+50)

			initiated = True
		else:
			# update the pannels
			panelA.configure(image=image)
			panelB.configure(image=output)
			panelA.image = image
			panelB.image = output



if __name__=="__main__":
	window = Tk()
	window.geometry('1166x718')
	window.resizable(0, 0)
	# window.state('zoomed')
	window.title('GUI')	

	canvas=Canvas(window, width=1166, height=718)
	canvas.pack()
	canvas.create_line(583,450,583,0, fill="black", width=3)	
	# canvas.create_line(0,550,1166,550, fill="black", width=3)	

	show_images('input.png', 'output.png')

	lgn_button = Image.open('select.png')
	lgn_button = lgn_button.resize([250, 50])
	photo = ImageTk.PhotoImage(lgn_button)
	lgn_button_label = Label(image=photo, bg=bg_color)
	lgn_button_label.image = photo
	lgn_button_label.place(x=int(718/2)+115, y=title_size+575)
	# login = Button(lgn_button_label, text='', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
	# 					bg='#EBEBEB', cursor='hand2', activebackground='#EBEBEB', fg='white', command=lambda: process_show(filedialog.askopenfilename()))
	lgn_button_label.bind("<Button-1>",lambda e: process_show(filedialog.askopenfilename()))
	# login.place(x=20, y=title_size+10)	

	result_label = Label(text="Result: -", bg=bg_color, fg="black",
								font=("yu gothic ui", 17, "bold"), justify="center")
	result_label.place(x=int(718/2 - 50)+100+(718/2), y=title_size+0)	

	input_label = Label(text="Input Sample", bg=bg_color, fg="black",
								font=("yu gothic ui", 17, "bold"))
	input_label.place(x=200, y=title_size+0)	

	time_card_img = Image.open('time.png')
	time_card_img = time_card_img.resize([300, 75])
	time_card_pht = ImageTk.PhotoImage(time_card_img)
	time_card = Label(image=time_card_pht, bg=bg_color)
	time_card.image = time_card_pht
	time_card.place(x=100, y=title_size+475)

	classification_card_img = Image.open('classification.png')
	classification_card_img = classification_card_img.resize([300, 75])
	classification_card_pht = ImageTk.PhotoImage(classification_card_img)
	classification_card = Label(image=classification_card_pht, bg=bg_color)
	classification_card.image = classification_card_pht
	classification_card.place(x=100+300+50, y=title_size+475)

	confidence_card_img = Image.open('confidence.png')
	confidence_card_img = confidence_card_img.resize([300, 75])
	confidence_card_pht = ImageTk.PhotoImage(confidence_card_img)
	confidence_card = Label(image=confidence_card_pht, bg=bg_color)
	confidence_card.image = confidence_card_pht
	confidence_card.place(x=100+300+50+300+50, y=title_size+475)	

	title_label = Label(text="Lung Disease Classification", bg=bg_color, fg="black",
								font=("yu gothic ui", 28, "bold"), justify="center")
	title_label.place(x=int(718/2), y=0)

	loading_label = Label(text="3.000 seconds", bg=bg_color, fg="black",
								font=("yu gothic ui", 17, "bold"), justify="center")
	loading_label.place(x=160, y=title_size+480)

	clf_label = Label(text="Lung Cancer 3", bg=bg_color, fg="black",
								font=("yu gothic ui", 17, "bold"), justify="center")
	clf_label.place(x=170+50+300, y=title_size+480)

	conf_label = Label(text="96.0007%", bg=bg_color, fg="black",
								font=("yu gothic ui", 17, "bold"), justify="center")
	conf_label.place(x=170+50+300+50+300+25, y=title_size+480)

	# time_card.place(x=int(718/2 - 50)+100+(718/2)+50, y=title_size+600)
	# while True:
	# 	try:
	# 		window.update_idletasks()
	# 		window.update()	
	# 	except KeyboardInterrupt:
	# 		break
	window.mainloop()