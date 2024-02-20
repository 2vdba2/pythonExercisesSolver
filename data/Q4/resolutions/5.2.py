#Prova Real
r=a+b
theta=np.deg2rad(thetad)
T,RA,RB = sy.symbols('T RA RB')
#a,b,theta, r, F1, F2, F3 = sy.symbols(r'a b \theta r F_1 F_2 F_3')
aplicacao=[
    [0,0,0],
    [b,0,0],
    [r*sy.cos(theta),r*sy.sin(theta),0],
    [0,r,0],
    [r,0,0],
    [0,r,0]]
vT   =T *vector(0,0,1)
vF1  =F1*vector(0,0,-1)
vF2  =F2*vector(0,0,-1)
vF3  =F3*vector(0,0,-1)
vRA  =RA*vector(0,0,1)
vRB  =RB*vector(0,0,1)

Forcas=[vT,vF1,vF2,vF3,vRA,vRB]
icognitas=[RA,RB,T]
RA=solveForces(Forcas,aplicacao,icognitas)[0]
resposta(RA,'N')
