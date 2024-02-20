
l1=a-c
h1=c
A1=l1*h1 
dx1=a/2
dy1=b/2+c/2
IAxy1=A1*dx1*dy1
Ibxy1=0
Ibx1=l1*h1**3/12
Iby1=l1**3*h1/12
IAx1=A1*dy1**2
IAy1=A1*dx1**2
Ix1=IAx1+Ibx1
Iy1=IAy1+Iby1
Ixy1=IAxy1+Ibxy1

l2=c
h2=b+2*c
A2=l2*h2
dx2=0
dy2=0 
IAxy2=0
Ibxy2=0
IAx2=A2*dy2**2
IAy2=A2*dx2**2
Ibx2=l2*h2**3/12
Iby2=l2**3*h2/12
Ix2=IAx2+Ibx2
Iy2=IAy2+Iby2
Ixy2=IAxy2+Ibxy2

l3=a-c
h3=c
A3=l3*h3
dx3=-a/2
dy3=-b/2-c/2
IAxy3=A3*dx3*dy3
Ibxy3=0
Ibx3=l3*h3**3/12
Iby3=l3**3*h3/12
IAx3=A3*dy3**2
IAy3=A3*dx3**2
Ix3=IAx3+Ibx3
Iy3=IAy3+Iby3
Ixy3=IAxy3+Ibxy3

Ix=Ix1+Ix2+Ix3 
Iy=Iy1+Iy2+Iy3 
Ixy=Ixy1+Ixy2+Ixy3

IxyMax=(Ix+Iy)/2+(((Ix-Iy)/2)**2+Ixy**2)**0.5
IxyMin=(Ix+Iy)/2-(((Ix-Iy)/2)**2+Ixy**2)**0.5
resposta(IxyMin,'m^4') 
