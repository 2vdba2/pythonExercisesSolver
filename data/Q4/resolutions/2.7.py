r=a+b
theta=np.deg2rad(thetad)
RBz=F2*sy.sin(theta)+F3
RAz=(F1*b+F2*r*sy.cos(theta))/r
T=F1+F2+F3-RAz-RBz
resposta(T,'N')
