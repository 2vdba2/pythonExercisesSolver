x=sy.symbols('x')
F=w*a
FRAx=0
FRBy=(-P*b+MC+a*F/2)/a
FRAy=-FRBy+F+P 
Vc1=-P
Mf1=Vc1*x
Vc2=Vc1+FRAy-w*(x-b) 
Mf2=Mf1.subs(x,b)+sy.integrate(Vc2,(x,b,x))

Vc3=0
Mf3=Mf2.subs(x,a+b)
Vc4=0
Mf4=0

R=Vc2.coeff(x)
C=Vc2.subs(x,0)
Q=Mf2.coeff(x**2)
J=Mf2.coeff(x)
D=Mf2.subs(x,0)


resposta(D,'')
