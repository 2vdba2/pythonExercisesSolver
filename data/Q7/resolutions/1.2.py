#b1,b2,h,x,y=sy.symbols('b1 b2 h x y')
y=sy.symbols('y')
x1=b1*y**2/h**2
x2=(-y/h+(1+b1/b2))*b2
V=sy.integrate((x2-x1),(y,0,h))
ycminf=y
xcminf=(x2+x1)/2
ycm=sy.integrate(ycminf*(x2-x1),(y,0,h))/V
xcm=sy.integrate(xcminf*(x2-x1),(y,0,h))/V
resposta(xcm,'m')
