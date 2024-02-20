F,B,D = sy.symbols('F B D')
#a,b,theta, r, F1, F2, F3 = sy.symbols(r'a b \theta r F_1 F_2 F_3')
aplicacao=[
    [b,0,0],
    [0,0,0],
    [0,a,0],
    [x,y,0]]
vF  =F*vector(0,0,1)
vB  =B*vector(0,0,1)
vD  =D*vector(0,0,1)
vP  =P*vector(0,0,-1)

Forcas=[vF,vB,vD,vP]
icognitas=[F,B,D]
res=solveForces(Forcas,aplicacao,icognitas)[-1]
resposta(res,'kN')
