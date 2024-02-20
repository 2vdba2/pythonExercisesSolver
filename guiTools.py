import gvar
from layout import *
from natsort import natsorted

def nextQuestion(questao,nQuestions):
	if(questao+1<(nQuestions)):
		questao+=1
	else:
		questao=0
	print('question =',questao)
	return questao

def previousQuestion(questao,nQuestions):

	if(questao<=0):
		questao=nQuestions-1
	else:
		questao-=1
	print('question =',questao)
	return questao

def nextQuestionGUI():
	for i in range(gvar.nQuestions): #use it instead of while(true) to avoid infinite loop
		try:
			gvar.questao=nextQuestion(gvar.questao,gvar.nQuestions)
			updateLayout()
			break
		except Exception as error:
			print("nao ha arquivos de input e output da questao =",gvar.exerciseIDList[gvar.questao])
			print(error)
	gvar.window.refresh()
	gvar.window["outputColumn"].contents_changed() # update column height


def previousQuestionGUI():
	#Verificar se há arquivos de input e output
	for i in range(gvar.nQuestions): #use it instead of while(true) to avoid infinite loop
		try:
			gvar.questao=previousQuestion(gvar.questao,gvar.nQuestions)
			updateLayout()
			break
		except Exception as error:
			print("nao ha arquivos de input e output da questao =",gvar.exerciseIDList[gvar.questao])
			print(error)

def changeFolder(event):
	gvar.questionDir= gvar.values[event]
	gvar.questao=0
	print('questionDir=',gvar.questionDir)
	print('questao=',gvar.questao)
	gvar.exerciseIDList=os.listdir('data/'+gvar.questionDir+'/images/') ### update exercises list
	gvar.nQuestions=len(gvar.exerciseIDList)
	for i in range(gvar.nQuestions):
		gvar.exerciseIDList[i]=gvar.exerciseIDList[i].rsplit('.', maxsplit=1)[0]#remove extension
	gvar.exerciseIDList=natsorted(gvar.exerciseIDList)
	updateLayout()

def calculate():

	#--------------------------
	# Get input and output data
	#--------------------------
	#update input
	for i in range(gvar.nInputs):
		inputVarValue="inputVarValues["+str(i)+"]"
		inputVarName="inputVarNames["+str(i)+"]"
		gvar.inputVarValues[i]=gvar.values[inputVarValue]
	#update output
	gvar.outputVarNames,gvar.outputVarValues,gvar.nOutputs=processOutputFile(gvar.outFileName)


	#---------------------------
	#Place output data
	#---------------------------
	for i in range(gvar.nOutputs):
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

		gvar.window[outputVarValue].update(gvar.outputVarValues[i])
	gvar.window["resposta"].update(gvar.stringResposta)

def about():
	text="O material que aqui se encontra, salvo quando citado/indicado, é de autoria de Vitor Dal Bó Abella e está licenciado com uma Licença Creative Commons - Atribuição-NãoComercial-CompartilhaIgual 4.0 Internacional (CC BY-NC-SA 4.0). \n\
\n\
Todas as imagens das questões foram retiradas do material de autoria de Rafael Antônio Comparsi Laranja  da disciplina de Mecanica Aplicada da UFRGS que estava licenciado com uma Licença Creative Commons - Atribuição-NãoComercial-CompartilhaIgual 4.0 Internacional (CC BY-NC-SA 4.0). \n\
\n\
Para saber mais sobre os tipos de licença, visite: https://creativecommons.org/licenses/by-nc-sa/4.0/"

	sg.popup(text, title='Sobre')

def intructions():
	text="\
	Na raiz do programa tem a pasta data. Nela estao todos os dados para montar o resolvedor de questoes\n\
	Dentro de data, ha uma pasta para cada questionario: Q1,Q2,Q3...\n\
	Dentro de cada pasta de questionario tem tres pastas: images, inputs e resolutions.\n\
	\n\
	Exemplo no questionario Z_Exemplo questao 1.1\n\
	Em images esta a imagem da questao salva como 1.1.png\n\
	\n\
	Em inputs esta o input da questao escrito em python salvo como 1.1.py:\n\
	a=2\n\
	b=3\n\
	\n\
	Em resolutions esta a resolucao da questao em python salvo como 1.1.py. No final da resolucao é chamada a funcao resposta(A,'m^2') para identificar a resposta:\n\
	A=a*b\n\
	resposta(A,'m^2')\n\
	\n\
	Para adicionar questoes, voce pode adicionar a um questionario ou criar um novo, desde que siga o padrao\n\
	"
	sg.popup(text, title='Como adicionar questões?')
