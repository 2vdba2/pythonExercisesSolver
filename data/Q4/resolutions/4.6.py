theta=np.deg2rad(thetad)
RAy=(-modPL*(a-c)-modPC*d+b/sy.tan(theta)*(modPL+modPC))/(c+b/sy.tan(theta))
RAx=(RAy-modPL-modPC)/sy.tan(theta)
modT=-RAx/sy.cos(theta)
resposta(RAx,'kN')
