from processFilesTools import *
from resolutionTools import *
from natsort import natsorted
from layout import *
from guiTools import *

# Build first Layout
layout=makeLayout()
gvar.window = sg.Window("Mecanica Aplicada", layout,resizable=False).Finalize()
updateLayout()

# Create an event loop
while True:
	event, gvar.values = gvar.window.read()

	if(event == "Calcular" ):
		print("Calculate")
		calculate()

	elif(event == "Proximo" ):
		print("Next")
		nextQuestionGUI()

	elif(event == "Anterior" ):
		print("Previous")
		previousQuestionGUI()

	elif(event=='-QCHOOSER-'):
		print("SelectFolder")
		changeFolder(event)

	elif(event=='Sobre'):
		print("About")
		about()
	elif(event=='Como adicionar questões?'):
		intructions()

	elif(event == "Exit" or event == sg.WIN_CLOSED):
		print("Exit")
		gvar.window.close()
		break
		

gvar.window.close()
