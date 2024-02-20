alpha=np.radians(alphad)
theta=sy.atan(modF*sy.cos(alpha)/(modFr-modF*sy.sin(alpha)))
T=modF*sy.cos(alpha)/sy.sin(theta)
resposta(T,'N')
