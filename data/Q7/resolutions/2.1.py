xcm1= b / 2
ycm1= (a + b) / 2
b1=b
h1= a - b
A1=b1*h1

xcm2= (a+b) / 2
ycm2= b / 2
b2=(a+b)
h2=b
A2=b2*h2

xcm=(A1*xcm1+A2*xcm2)/(A1+A2)
ycm=(A1*ycm1+A2*ycm2)/(A1+A2)

##### 1

Ibx1=b1*h1**3/12
Iby1=b1**3*h1/12

dy1=-ycm+ycm1
dx1=-xcm+xcm1

Ix1=Ibx1+A1*dy1**2
Iy1=Iby1+A1*dx1**2
Ixy1=A1*dx1*dy1

###### 2

Ibx2=b2*h2**3/12
Iby2=b2**3*h2/12

dx2=-xcm+xcm2
dy2=-ycm+ycm2

Iy2=Iby2+A2*dx2**2
Ix2=Ibx2+A2*dy2**2
Ixy2=A2*dx2*dy2

## ALL

Ix=Ix1+Ix2
Iy=Iy1+Iy2
Ixy=Ixy1+Ixy2


IxyMax=(Ix+Iy)/2+(((Ix-Iy)/2)**2+Ixy**2)**0.5
IxyMin=(Ix+Iy)/2-(((Ix-Iy)/2)**2+Ixy**2)**0.5
theta=sy.atan(2*Ixy/(Iy-Ix))/2
thetadeg=theta*180/np.pi
resposta(xcm,'mm')
