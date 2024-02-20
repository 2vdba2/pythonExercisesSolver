h1=2*c
l1=a
dx=2/3*a
Iby1=l1**3*h1/36
A1=h1*l1/2
Iy1=Iby1+A1*dx**2
Iby2=np.pi*r**4/4 
A2=np.pi*r**2 
dx2=a+b
Iy2=Iby2+A2*dx2**2
l3=2*b 
h3=2*c
Iby3=l1**3*h1/12 
A3=l3*h3
dx3=a+b 
Iy3=Iby3+A3*dx3**2 
Iy=Iy1+Iy3-Iy2

x1cm=2/3*a 
y1cm=(2*c)/3
x2cm=a+b
y2cm=c 

xcm=(A1*x1cm+(A3-A2)*x2cm)/(A1+(A3-A2))
ycm=(A1*y1cm+(A3-A2)*y2cm)/(A1+(A3-A2))

resposta(ycm,'m') 

