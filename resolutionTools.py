import gvar
import inspect
import os
import numpy as np
import sympy as sy
from sympy.vector import CoordSys3D
import time
import gvar

N = CoordSys3D('N')
i=N.i
j=N.j
k=N.k

def norm(BC):
	return sy.sqrt(BC.dot(BC))
def unit(BC):
	return BC/norm(BC)
def projectNorm(v1,v2):
	#projeta v1 em v2
	return v1.dot(unit(v2))
def vector(a,b,c):
	return a*i+b*j+c*k
def subValues(exp,symbolVector,valuesVector):
	for i in range(len(symbolVector)):
		exp=exp.subs(symbolVector[i],valuesVector[i])
	return exp
def angle(v1,v2):
	cos=unit(v1).dot(unit(v2))
	ang=sy.acos(cos)
	return ang #RADIANS!
def solveForces(Forcas,aplicacao,icognitas,debugON=False):
	n=len(Forcas)
	vetorAplicacao=[]
	for f in range(n):
		vetorAplicacao.append(vector(*aplicacao[f]))

	#Somatorio das forcas
	dir=[i,j,k]
	somaF=[0,0,0]
	for f in range(n):
		for d in range(3):
			somaF[d]+=Forcas[f].dot(dir[d])
	#Somatorio dos momentos
	somaM=[0,0,0]
	for f in range(n):
		for d in range(3):
			somaM[d]+=(vetorAplicacao[f].cross(Forcas[f])).dot(dir[d])
	#Resolver equacoes
	equacoes=somaF+somaM
	equacoes = [i for i in equacoes if i != 0] #eliminar zeros
	result=sy.solve(equacoes,*icognitas)
	print(result)
	res=[]

	if(debugON):
		print('Forcas')
		print(Forcas)
		print('Equacoes')
		print(equacoes)
	for icog in range(len(icognitas)):
		res.append(result[icognitas[icog]])

		
	return res
	
def resposta(r,unidade):
	if(unidade==r'^{\circ}'):
		unidade="°"
		r=np.rad2deg(float(r))
	try:
		gvar.stringResposta='{0:.2f}'.format(r)+unidade
	except:
		pass
	unidadeResposta=unidade
	print('A resposta final é:',gvar.stringResposta)
