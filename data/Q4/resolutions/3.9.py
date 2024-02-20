#Prova Real
aplicacao=[
    [0,0,0], #RA
    [a+b,0,0], #Tbd
    [a+b,d+e,0], #Tcd
    [a,d+e,0],
    [a+b,d,0]]
aplicacao
Tbd,Tcd,Tef,RAx,RAy,RAz = sy.symbols('Tbd Tcd Tef RAx RAy RAz')
vTbd=Tbd*vector(0,0,1)
vTef=Tef*vector(0,0,1)
vTcd=Tcd*1/(sy.sqrt((d+e)**2+c**2))*vector(-d-e,c,0)
vP  =P*vector(0,0,-1)
vRA=vector(RAx,RAy,RAz)

Forcas=[vRA,vTbd,vTcd,vTef,vP]
icognitas=[RAx,RAy,RAz,Tbd,Tcd,Tef]
res=solveForces(Forcas,aplicacao,icognitas)[3]
resposta(res,'kN')
