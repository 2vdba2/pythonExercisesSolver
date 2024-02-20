alphaRad=np.radians(alpha)
thetaRad=np.radians(theta)


P=modP*vector(sy.cos(alphaRad),-sy.sin(alphaRad),0)
W=modW*vector(-sy.cos(thetaRad),-sy.sin(thetaRad),0)
F=modF*vector(1,0,0)
R=P+W+F
modR=norm(R)
resposta(modR,'N')
