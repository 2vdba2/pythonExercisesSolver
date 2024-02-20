H=(a**2+(b-c)**2)**0.5
RCx,RCy,x = sy.symbols('RCx RCy x')
aplicacao=[[a,c,0],[x,0,0],[0,0,0],[0,0,0]]
vT=T*vector(-a/H,(b-c)/H,0)
vP=P*vector(0,-1,0)
vRCx=RCx*vector(1,0,0)
vRCy=RCy*vector(0,1,0)
Forcas=[vT,vP,vRCx,vRCy]
icognitas=[x,RCx,RCy]
x=solveForces(Forcas,aplicacao,icognitas)[0]
resposta(x,'m')
