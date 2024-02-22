#h,a=sy.symbols('h a',real=True,positive=True)
x=sy.symbols('x',real=True,positive=True)
y=h*x**2/a**2
Iy=sy.simplify(sy.integrate(x**2*(h-y),(x,0,a)))

y=sy.symbols('y',real=True,positive=True)
x=sy.sqrt((y*a**2/h))
Ix=sy.simplify(sy.integrate(y**2*x,(y,0,h)))
resposta(Iy,'m^4')
