theta=np.deg2rad(thetad)
L=a/2/sy.cos(theta)
P1=a*d*g
P2=4*L*d*g
P3=2*a*d*g
RCy=(P1+P2+P3)/2
FEAy=RCy-(3*L+2*a)*d*g-L*d*g/2-a*d*g/2
FEA=FEAy/sy.sin(theta)

FBDy=RCy-(3/2*L+a)*d*g
FBD=FBDy/sy.sin(theta)
FCD=FEA

FBDx=FBD*sy.cos(theta)
FCDx=FCD*sy.cos(theta)
FDE=FCDx-FBDx

resposta(FDE,'N')