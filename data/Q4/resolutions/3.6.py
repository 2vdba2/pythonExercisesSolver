#Prova Real
theta=np.deg2rad(thetad)
aplicacao=[
    [0,0,0],
    [0,r,0],
    [r*sy.sin(theta),r*(1+sy.cos(theta)),0]]
aplicacao
RAx,RAy,RAz,T = sy.symbols('RAx RAy RAz T')

vRA =    vector(RAx,RAy,RAz)
vP  =P  *vector(0,0,-1)
vT  =T  *unit(vector(r*sy.sin(theta),r*(1+sy.cos(theta)),2*r))
#print(vT)
Forcas=[vRA,vP,vT]
#print(Forcas)

#print(icognitas)
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

MAy,MAz = sy.symbols('MAy MAz')

somaM=[0,MAy,MAz]
for f in range(n):
    for d in range(3):
        somaM[d]+=(vetorAplicacao[f].cross(Forcas[f])).dot(dir[d])
#Resolver equacoes
equacoes=somaF+somaM
equacoes = [i for i in equacoes if i != 0] #eliminar zeros
#print(equacoes)
icognitas=[RAx,RAy,RAz,T,MAy,MAz]
result=sy.solve(equacoes,*icognitas)
print(result)
res=[]
for icog in range(len(icognitas)):
    res.append(result[icognitas[icog]])
RAx=res[0]
RAy=res[1]
RAz=res[2]
T=res[3]
MAy=res[4]
MAz=res[5]
resposta(res[3],'N')
