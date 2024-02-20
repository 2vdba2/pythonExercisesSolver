alpha=np.radians(alpha)
theta=np.radians(theta)
F1=modF1*vector(4/5,-3/5,0)
F2=modF2*vector(-sy.sin(theta),-sy.cos(theta),0)
F3=modF3*vector(-sy.sin(alpha),sy.cos(alpha),0)
F=F1+F2+F3
modF=norm(F)
resposta(modF,'N')
