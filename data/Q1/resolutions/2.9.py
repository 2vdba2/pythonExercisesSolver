A=np.radians(A)
F1=modF1*vector(0,1,0)
F2=modF2*vector(sy.cos(A),-sy.sin(A),0)
F=F1+F2
theta=sy.atan(F.dot(j)/F.dot(i))
resposta(theta,r'^{\circ}')
