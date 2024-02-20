theta=np.deg2rad(thetad)
Rx=-P*sy.sin(theta)/(2*(1+sy.cos(theta)))
Rz=P*(1-1/(1+sy.cos(theta)))
Ry=-P/2
resposta(Rz,'N')
