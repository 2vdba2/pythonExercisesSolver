theta=np.deg2rad(thetad)
L0=a-b
Lf=sy.sqrt((a-b*sy.cos(theta))**2+(b*sy.sin(theta))**2)
T=Lf*P/(2*a*sy.tan(theta))
kcte=T/(Lf-L0)
resposta(kcte,'N/m')
