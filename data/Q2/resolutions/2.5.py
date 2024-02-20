theta2=np.radians(theta2d)
theta1, modFAB=sy.symbols(r'\theta_1 |F_{AB}|',real=True, positive=True)
F=modF*vector(0,-1,0)
FAC=modFAC*vector(-sy.cos(theta1),sy.sin(theta1),0)
FAB=modFAB*vector(sy.cos(theta2),sy.sin(theta2),0)
eq=F+FAC+FAB
eq1=eq.dot(i)
eq2=eq.dot(j)
theta1val, modFABval=sy.solve([eq1,eq2],(theta1,modFAB))[0]
theta1deg=np.rad2deg(float(theta1val))
h=a*sy.sin(theta2)
L=h/sy.sin(theta1val)
resposta(L,'m')
