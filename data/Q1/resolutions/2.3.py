theta=np.radians(theta)
beta=np.radians(40)
FA=modFA*vector(sy.sin(theta),sy.cos(theta),0)
FB=modFB*vector(sy.sin(beta),-sy.cos(beta),0)
F=FA+FB
modF=norm(F)
resposta(modF,'kN')
