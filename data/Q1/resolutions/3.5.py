theta=np.radians(thetad)
xP=a
yP=b-c
zP=-d
HP=(xP**2+yP**2+zP**2)**0.5 #hipotenusa P
xF=a*sy.cos(theta)
yF=a*sy.sin(theta)+b
zF=-d
HF=(xF**2+yF**2+zF**2)**0.5 #hipotenusa F
F =modF *vector(xF/HF,yF/HF,zF/HF)
P =modP *vector(xP/HP,yP/HP,zP/HP)
Fr=F+P
modFr=norm(Fr)
resposta(modFr,'N')
