import PySimpleGUI as sg
from processFilesTools import *
from resolutionTools import *

def makeLayout():

	#----------
	#Right Side
	#----------
	#Input
	inputGUI = [[None for _ in range(3)] for _ in range(gvar.outputColumnMaxSize)]
	for i in range(gvar.outputColumnMaxSize):
		inputVarName="inputVarNames["+str(i)+"]"
		inputVarValue="inputVarValues["+str(i)+"]"
		inputGUI[i][0]= sg.Text(inputVarName,key=inputVarName,visible=False)
		inputGUI[i][1]= sg.Push()
		inputGUI[i][2]= sg.In(inputVarValue,size=(10, 1), enable_events=True, key=inputVarValue,visible=False)
	inputGUI=[[sg.Text("Input")]]+inputGUI
	
	#Output
	outputGUI = [[None for _ in range(3)] for _ in range(gvar.outputColumnMaxSize)]
	for i in range(gvar.outputColumnMaxSize):
		outputVarName="outputVarNames["+str(i)+"]"
		outputVarValue="outputVarVaues["+str(i)+"]"
		outputGUI[i][0]= sg.Text(outputVarName,key=outputVarName,visible=False)
		outputGUI[i][1]= sg.Push()
		outputGUI[i][2]= sg.InputText(outputVarValue,size=(20, 1),use_readonly_for_disable=True, disabled=True, enable_events=True, key=outputVarValue,visible=False)

	outputGUI=[[sg.Text("Output")]]+outputGUI

	#------------
	#Left Side
	#------------
	lst = sg.Combo(gvar.questionDirList, default_value=gvar.questionDir,font=('Arial Bold', 14), enable_events=True,  readonly=True, key='-QCHOOSER-') #escolher questionario
	top = 	[[lst],\
			[sg.Text("exerciseIDList[gvar.questao]",key="exerciseIDList[gvar.questao]")],\
			[sg.Button("Anterior"),sg.Button("Proximo")],\
			[sg.Image(gvar.defaultImage,key="imageEnunciado")]]

	#-------------
	# Build Layout
	#-------------
	bottom=[sg.Button("Exit"),sg.Push(),sg.Button('Sobre'),sg.Button('Como adicionar questões?'),sg.Push(),sg.Text("resposta: ",visible=True),sg.Text("resposta", enable_events=True, key="resposta",visible=True),sg.Button("Calcular")]
	topColumn= sg.Column(top,expand_y=True,expand_x=True)
	inputColumn=sg.vtop(sg.Column(inputGUI))
	outputColumn=sg.vtop(sg.Column(outputGUI, scrollable=True,  vertical_scroll_only=False,size=(230,800),vertical_alignment='center',justification='center',key="outputColumn"))
	layout = [[ topColumn      ,sg.VSeperator(),inputColumn,outputColumn],bottom]
	#pyperclip.copy(gvar.stringResposta)

	return layout

def updateLayout():
	print("UPDATE LAYOUT!")
	#------------
	#Reset layout
	#------------
	for i in range(gvar.outputColumnMaxSize):
		inputVarName="inputVarNames["+str(i)+"]"
		inputVarValue="inputVarValues["+str(i)+"]"
		outputVarName="outputVarNames["+str(i)+"]"
		outputVarValue="outputVarVaues["+str(i)+"]"
		gvar.window[inputVarName].update(visible=False)
		gvar.window[inputVarValue].update(visible=False)
		gvar.window[outputVarName].update(visible=False)
		gvar.window[outputVarValue].update(visible=False)
	#--------------------------
	# Get input and output data
	#--------------------------
	gvar.inFileName="./data/"+gvar.questionDir+"/inputs/"+gvar.exerciseIDList[gvar.questao]+".py"
	gvar.outFileName="./data/"+gvar.questionDir+"/resolutions/"+gvar.exerciseIDList[gvar.questao]+".py"
	
	gvar.inputVarNames,gvar.inputVarValues,gvar.nInputs=processInputFile(gvar.inFileName)
	gvar.outputVarNames,gvar.outputVarValues,gvar.nOutputs=processOutputFile(gvar.outFileName)

	#---------------------------
	#Place input and output data
	#---------------------------
	gvar.window["exerciseIDList[gvar.questao]"].update(gvar.exerciseIDList[gvar.questao])
	for i in range(gvar.nInputs):
		inputVarName="inputVarNames["+str(i)+"]"
		inputVarValue="inputVarValues["+str(i)+"]"
		gvar.window[inputVarName].update(gvar.inputVarNames[i],visible=True)
		gvar.window[inputVarValue].update(gvar.inputVarValues[i],visible=True)
	
	for i in range(gvar.nOutputs):
		outputVarName="outputVarNames["+str(i)+"]"
		outputVarValue="outputVarVaues["+str(i)+"]"
		#round outputVarValues[i]
		try: #Float
			gvar.outputVarValues[i]="{:.2f}".format(gvar.outputVarValues[i])
		except:
			try:
				for a in sy.preorder_traversal(gvar.outputVarValues[i]):
					if isinstance(a, sy.Float):
						gvar.outputVarValues[i] = gvar.outputVarValues[i].subs(a, round(a, 2))
			except:
				print("Round didnt work")
		
		gvar.window[outputVarName ].update(gvar.outputVarNames[i] ,visible=True)
		gvar.window[outputVarValue].update(gvar.outputVarValues[i],visible=True)

		
	gvar.window["resposta"].update(gvar.stringResposta)
	imageEnunciado="./data/"+gvar.questionDir+"/images/"+gvar.exerciseIDList[gvar.questao]+".png"
	gvar.window["imageEnunciado"].update(imageEnunciado)
