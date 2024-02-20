x = sy.symbols("x", real=True, positive=True) 
#h,b1,b2 = sy.symbols("h b1 b2", real=True, positive=True) 
y1=h/(b1**0.5)*x**0.5 
Iy1=sy.integrate(x**2*y1,(x,0,b1)) 
y2=h*((1+b1/b2)-x/b2) 
Iy2=sy.simplify(sy.integrate(x**2*y2,(x,b1,b1+b2)))
Iy=Iy1+Iy2
resposta(Iy,'m^4')

