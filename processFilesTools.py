import gvar
from resolutionTools import *
import os

def removeEmptyLines(text):
	text = os.linesep.join([s for s in text.splitlines() if s])
	return text

#Executa codigo e extrai nome e valores das variaveis locais
def getVarsNExec(code0):
	exec(code0)
	tmp = locals().copy()
	varNames=[]
	varValues=[]
	print(tmp.items())
	for k,v in tmp.items():
		if(not k.startswith('_') and k!='tmp' and k!='code0' and k!='In' and k!='Out' and not hasattr(v, '__call__') and  not str(v).startswith('<')):
			#print(kkk)
			varNames.append(k)
			varValues.append(v)
	#print("getVarsNExec FUNCIONNN")
	#print(varNames)
	#print(varValues)
	return varNames,varValues,len(varNames)

def getVarsNExecFromFile(filename):
	with open(filename,"r") as ffff:
		code0 = ffff.read()
	varNames,varValues,lenVar=getVarsNExec(code0)
	return varNames,varValues,lenVar

#Processa input file e pega as variaveis de input e seus valores
def processInputFile(filename):
	inputVarNames,inputVarValues,nInputs=getVarsNExecFromFile(filename)
	return inputVarNames,inputVarValues,nInputs

#Processa output file com valores de input padrao
def processOutputFile(filename):
	#Turn inputVars global
	for i in range(gvar.nInputs):
		exec(gvar.inputVarNames[i]+'='+str(gvar.inputVarValues[i]),globals())
	#update output
	outputVarNames,outputVarValues,nOutputs=getVarsNExecFromFile(filename)
	return outputVarNames,outputVarValues,nOutputs
	#print(inputVarNames)
	#print(inputVarValues)
