F1=modF1*vector(1,0,0)
F2=modF2*vector(3/5,4/5,0)
F12=F1+F2
modF12=norm(F12)
theta=sy.atan(F12.dot(j)/F12.dot(i))
resposta(theta,r'^{\circ}')
