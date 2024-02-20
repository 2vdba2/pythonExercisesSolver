a=(d1**2+d3**2)**0.5
b=(d2**2+d3**2)**0.5
c=(d1**2+d2**2)**0.5
theta=sy.acos((a**2+b**2-c**2)/(2*a*b))
resposta(theta,r'^{\circ}')
