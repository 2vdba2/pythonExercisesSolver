theta3=90-theta1-theta2
theta1=np.radians(theta1)
theta2=np.radians(theta2)
theta3=np.radians(theta3)
modV=modF*sy.cos(theta2+theta3)/sy.cos(theta3)
modU=modF*sy.cos(theta1)-modV*sy.cos(theta2+theta1)
resposta(modU,'N')
