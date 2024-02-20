theta2=np.radians(theta2deg)
theta3=np.radians(theta3deg)
modF3=5
modF4=7
theta1=sy.atan(-(modF2*sy.cos(theta2)+modF3*sy.sin(theta3)-3/5*modF4)/(modF2*sy.sin(theta2)-modF3*sy.cos(theta3)-modF4*4/5))
theta1deg=np.rad2deg(float(theta1))
resposta(theta1,'^{\circ}')
