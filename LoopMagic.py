import PySimpleGUI as sg

sg.change_look_and_feel('LightGrey6')

background = sg.LOOK_AND_FEEL_TABLE['LightGrey6']['BACKGROUND']

track_1=[[sg.Button(image_filename = './img/EDIT.png', image_size=(96,41), button_color=('white',background), border_width=0, key = ('-edit1-'))],
		 [sg.Text("CLEAR: HOLD > 2 SEC", font=("Orbitron", 9))],
		 [sg.Button(image_filename = './img/STOP.png', image_size=(93,93), button_color=('white',background), border_width=0, key = ('-stop1-')),
		 sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25)],
		 [sg.Button(image_filename = './img/OFF.png', image_size=(200,200), button_color=('white',background), border_width=0, key = ('-play1-'))]
		 ]
		 
track_2=[[sg.Button(image_filename = './img/EDIT.png', image_size=(96,41), button_color=('white',background), border_width=0, key = ('-edit2-'))],
		 [sg.Text("CLEAR: HOLD > 2 SEC", font=("Orbitron", 9))],
		 [sg.Button(image_filename = './img/STOP.png', image_size=(93,93), button_color=('white',background), border_width=0, key = ('-stop2-')),
		 sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25)],
		 [sg.Button(image_filename = './img/OFF.png', image_size=(200,200), button_color=('white',background), border_width=0, key = ('-play2-'))]
		 ]

track_3=[[sg.Button(image_filename = './img/EDIT.png', image_size=(96,41), button_color=('white',background), border_width=0, key = ('-edit3-'))],
		 [sg.Text("CLEAR: HOLD > 2 SEC", font=("Orbitron", 9))],
		 [sg.Button(image_filename = './img/STOP.png', image_size=(93,93), button_color=('white',background), border_width=0, key = ('-stop3-')),
		 sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25)],
		 [sg.Button(image_filename = './img/OFF.png', image_size=(200,200), button_color=('white',background), border_width=0, key = ('-play3-'))]
		 ]		 

track_4=[[sg.Button(image_filename = './img/EDIT.png', image_size=(96,41), button_color=('white',background), border_width=0, key = ('-edit4-'))],
		 [sg.Text("CLEAR: HOLD > 2 SEC", font=("Orbitron", 9))],
		 [sg.Button(image_filename = './img/STOP.png', image_size=(93,93), button_color=('white',background), border_width=0, key = ('-stop4-')),
		 sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25)],
		 [sg.Button(image_filename = './img/OFF.png', image_size=(200,200), button_color=('white',background), border_width=0, key = ('-play4-'))]
		 ]

logo=[[sg.Image(filename = './img/LOGO.png', size = (281,46), background_color = background)]]	
 
tracks=[[sg.Column(logo,justification = "center")],[sg.Column(track_1),sg.Column(track_2),sg.Column(track_3),sg.Column(track_4)]]
		 
menu = sg.Window('LoopMagic', tracks, use_default_focus=False)

pulse1=0
pulse2=0
pulse3=0
pulse4=0
edit1=False
edit2=False
edit3=False
edit4=False

while True:
		event,values = menu.Read()
		if(event == '-edit1-'):
			if(edit1==False):
				edit1=True
				menu['-edit1-'].update(image_filename='./img/EDIT_ON.png')
			else:
				edit1=False
				menu['-edit1-'].update(image_filename='./img/EDIT.png')	
		elif(event == '-play1-'):
			menu['-play1-'].update(image_filename='./img/REC.png')
		elif(event == '-edit2-'):
			if(edit2==False):
				edit2=True
				menu['-edit2-'].update(image_filename='./img/EDIT_ON.png')
			else:
				edit2=False
				menu['-edit2-'].update(image_filename='./img/EDIT.png')	
		elif(event == '-play2-'):
			menu['-play2-'].update(image_filename='./img/PLAY.png')
		elif(event == '-edit3-'):
			if(edit3==False):
				edit3=True
				menu['-edit3-'].update(image_filename='./img/EDIT_ON.png')
			else:
				edit3=False
				menu['-edit3-'].update(image_filename='./img/EDIT.png')	
		elif(event == '-play3-'):
			menu['-play3-'].update(image_filename='./img/REC.png')
		elif(event == '-edit4-'):
			if(edit4==False):
				edit4=True
				menu['-edit4-'].update(image_filename='./img/EDIT.png')
			else:
				edit4=False
				menu['-edit4-'].update(image_filename='./img/EDIT_ON.png')	
		elif(event == '-play4-'):
			menu['-play4-'].update(image_filename='./img/REC.png')						
		elif(event == '-stop1-'):
			menu['-play1-'].update(image_filename='./img/OFF.png')
		elif(event == '-stop2-'):
			menu['-play2-'].update(image_filename='./img/OFF.png')
		elif(event == '-stop3-'):
			menu['-play3-'].update(image_filename='./img/OFF.png')
		elif(event == '-stop4-'):
			menu['-play4-'].update(image_filename='./img/OFF.png')
				
