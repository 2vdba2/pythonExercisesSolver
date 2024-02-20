alpha=np.radians(alphad)
theta=sy.atan((4/5*modP-modW*sy.cos(alpha))/(modFr-modW*sy.sin(alpha)-3/5*modP))
resposta(theta,r'^{\circ}')
