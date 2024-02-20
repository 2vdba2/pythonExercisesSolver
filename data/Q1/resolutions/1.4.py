AB=vector(c,d-a,-b)
ABu=unit(AB)
F=modF*ABu
AO=vector(0,-a,-b)
AOu=unit(AO)
modFAO=F.dot(AOu)
resposta(modFAO,'N')
