DX=a-(f+e)
DY=c
DZ=b
H=(DX**2+DY**2+DZ**2)**0.5
#Prova Real
aplicacao=[
    [0,0,0],
    [-e,c,0],
    [-e-f,c,0]]
aplicacao
RAx,RAy,RAz,MAy,MAz,T = sy.symbols('RAx RAy RAz MAy MAz T')

vRA =    vector(RAx,RAy,RAz)
vP  =P  *vector(0,0,-1)
vT  =T  *vector(DX/H,DY/H,DZ/H)
Forcas=[vRA,vP,vT]
#print(Forcas)

#print(icognitas)
n=len(Forcas)
vetorAplicacao=[]
for ff in range(n):
    vetorAplicacao.append(vector(*aplicacao[ff]))

#Somatorio das forcas
dir=[i,j,k]
somaF=[0,0,0]
for ff in range(n):
    for d in range(3):
        somaF[d]+=Forcas[ff].dot(dir[d])
#Somatorio dos momentos


somaM=[0,MAy,MAz]
for ff in range(n):
    for d in range(3):
        somaM[d]+=(vetorAplicacao[ff].cross(Forcas[ff])).dot(dir[d])
#Resolver equacoes
equacoes=somaF+somaM
equacoes = [i for i in equacoes if i != 0] #eliminar zeros
print(equacoes)
icognitas=[RAx,RAy,RAz,T,MAy,MAz]
result=sy.solve(equacoes,*icognitas)
#print(result)
res=[]
for icog in range(len(icognitas)):
    res.append(result[icognitas[icog]])

resposta(-res[0],'kN')
