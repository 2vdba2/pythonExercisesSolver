#usar eixo x' como referencia
alpha=np.radians(alpha_deg)
fi=np.radians(fi_deg)
beta=sy.atan((modF*sy.sin(fi)+modF2*sy.sin(alpha))/(modF*sy.cos(fi)-modF2*sy.cos(alpha)-modF3))
theta=beta-fi
resposta(theta,r'^{\circ}')
