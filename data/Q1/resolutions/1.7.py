Arad=np.radians(A)
F2=vector(modF2,0,0)
F1=modF1*vector(sy.cos(Arad),sy.sin(Arad),0)
F=F1+F2
modF=norm(F)
resposta(modF,'kN')
