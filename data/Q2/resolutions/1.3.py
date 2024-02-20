modFCD=modP/d*(c**2+d**2)**0.5
modFCB=modP*c*((a**2+b**2)**0.5)/2/b/d
modFCA=modFCB
P=modP*vector(0,0,-1)
FCD=modFCD*vector(0,c/(c**2+d**2)**0.5,d/(c**2+d**2)**0.5)
FCB=modFCB*vector(-a/(a**2+b**2)**0.5,-b/(a**2+b**2)**0.5,0)
FCA=modFCB*vector(+a/(a**2+b**2)**0.5,-b/(a**2+b**2)**0.5,0)
resposta(modFCB,'N')
