theta1_val=np.radians(theta1d)
theta2_val=np.radians(theta2d)

theta1, theta2, theta3=sy.symbols(r'\theta_1 \theta_2 \theta_3',real=True, positive=True)
F, a, b=sy.symbols(r'F a b',real=True, positive=True)
h=b*sy.sin(theta1)
L=b*sy.cos(theta1)
d=sy.sqrt(h**2+(L+a)**2)
d=d.simplify()

theta3val=sy.atan(b*sy.sin(theta1)/(b*sy.cos(theta1)+a))

Fx=F*sy.cos(theta2)
Fy=F*sy.sin(theta2)
FRx=-Fx*sy.sin(theta3)
FRy=+Fy*sy.cos(theta3)
FR=FRx+FRy
FR=sy.simplify(FR)
FR=FR.subs(theta3,theta3val)
M=FR*d
symbolVector=[F,a,b,theta1,theta2]
valuesVector=[F_val,a_val,b_val,theta1_val,theta2_val]
Mvalue=subValues(M,symbolVector,valuesVector)
FRvalue=subValues(FR,symbolVector,valuesVector)
resposta(Mvalue,'N.m')
