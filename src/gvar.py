import os
from natsort import natsorted

stringResposta=''

#Frame
window=[]
values=[]

#Questions
questao=0
print(os.listdir('data'))
questionDirList=natsorted(os.listdir('data'))
questionDir=questionDirList[0]
exerciseIDList=os.listdir('data/'+questionDir+'/images/')
nQuestions=len(exerciseIDList)
for i in range(nQuestions):
	exerciseIDList[i]=exerciseIDList[i].rsplit('.', maxsplit=1)[0]#remove extension
exerciseIDList=natsorted(exerciseIDList)

#inputs
nInputs=0
inputVarNames=[]
inputVarValues=[]
inFileName=''

#outputs
nOutputs=0
outputVarNames=[]
outputVarValues=[]
outputColumnMaxSize=50
outFileName=''
