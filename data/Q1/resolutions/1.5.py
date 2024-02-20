alpha=np.radians(20)
F=modF*vector(-1,0,0)
FAC=modFAC*vector(-sy.cos(alpha),sy.sin(alpha),0)
FBA=F-FAC
beta=sy.atan(-FBA.dot(j)/FBA.dot(i))
theta=beta-alpha
resposta(theta,r'^{\circ}')
