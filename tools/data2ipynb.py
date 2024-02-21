import nbformat as nbf
from natsort import natsorted
import os as os
nb = nbf.v4.new_notebook()

exerciseIDList=natsorted(os.listdir('inputs/'))
nQuestions=len(exerciseIDList)

imports=open('beg', 'r').read()
notebook=[nbf.v4.new_code_cell(imports)]

for i in range(nQuestions):
	inputCode 	= "%%write_and_run inputs/{questao}.py\n"+open('inputs/'+exerciseIDList[i], 'r').read()
	outputCode 	= "%%write_and_run resolutions/{questao}.py\n"+open('resolutions/'+exerciseIDList[i], 'r').read()
	questionCode="\
questao="+"'"+exerciseIDList[i]+"'"+"\n\
display(Math(r'\Large{'+questao+')}'))\n\
Image(filename='images/'+questao+'.png') \n\
"
	
	imageCell=nbf.v4.new_code_cell(questionCode)
	inputCell=nbf.v4.new_code_cell(inputCode)
	OutputCell=nbf.v4.new_code_cell(outputCode)

	notebook.append(imageCell)
	notebook.append(inputCell)
	notebook.append(OutputCell)
	print(questionCode)
	print(inputCode)
	print(outputCode)

nb['cells'] = notebook
fname = 'test.ipynb'

with open(fname, 'w') as f:
    nbf.write(nb, f)
