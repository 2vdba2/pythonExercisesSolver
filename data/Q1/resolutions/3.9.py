BC=-c*i-a*j+b*k
CD=vector(-c,e,b)
CD=unit(CD)
F=modF*CD
modT=projectNorm(F,BC)
resposta(modT,'N')
