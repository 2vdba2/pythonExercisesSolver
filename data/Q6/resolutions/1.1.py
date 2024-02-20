#F*=1000
#w*=1000
#MC*=1000
By=(-MC+w*c**2/2)/c
FRAy=F+By
MA=F*a+By*(a+b)
x=sy.symbols('x')
V1=FRAy
V2=V1-F
V3=V2-w*(x-3)
M1=-MA+sy.integrate(V1,(x,0,x))
M2=M1.subs(x,2)+sy.integrate(V2,(x,a,x))
M3=M2.subs(x,3)+sy.integrate(V3,(x,a+b,x))

f=M2.subs(x,0)*1000
e=M2.coeff(x)*1000
resposta(f,'')
