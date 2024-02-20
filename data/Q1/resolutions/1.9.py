theta=np.radians(75)
F1=modF1*vector(1,0,0)
F2=modF2*vector(sy.cos(theta),sy.sin(theta),0)
F=F1+F2
modF=norm(F)
resposta(modF,'kN')
