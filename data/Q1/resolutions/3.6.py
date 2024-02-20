dx=L*sy.cos(60)
dy=L*sy.sin(60)
dz=a
LF=(dx**2+dy**2+dz**2)**0.5
F =modF/LF *vector(-dx,-dy,dz)
Du= 1/L*vector(-dx,-dy,0)
modT=F.dot(Du)
modT=modT.evalf()
resposta(modT,'N')
