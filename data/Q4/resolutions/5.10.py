theta=np.deg2rad(thetad)
RAx,RAy,RBx = sy.symbols('RAx RAy RBx')
#a,b,theta, r, F1, F2, F3 = sy.symbols(r'a b \theta r F_1 F_2 F_3')
aplicacao=[
    [0,0,0],
    [a,0,0],
    [a+b,0,0],
    [a+b+c+d*sy.cos(theta),d*sy.sin(theta),0]]
vRA  =vector(RAx,RAy,0)
vF1  =F1*vector(0,-1,0)
vF2  =F2*vector(0,-1,0)
vRB  =vector(RBx,0,0)

Forcas=[vRA,vF1,vF2,vRB]
icognitas=[RAx,RAy,RBx]
res=solveForces(Forcas,aplicacao,icognitas,True)[-1]
resposta(abs(res),'kN')
