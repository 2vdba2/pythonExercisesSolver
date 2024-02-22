xcm=[c/2,c-a/2,c/2]
ycm=[a/2,a+b/2,a+b+a/2]
h=[a,b,a]
l=[c,a,c]
dx=xcm
dy=np.array(ycm)-(a+b/2)
Iy=[None]*3
Ix=[None]*3
for i in range(3):
    Ix[i]=l[i]*h[i]**3/12+h[i]*l[i]*dy[i]**2
    Iy[i]=l[i]**3*h[i]/12+h[i]*l[i]*dx[i]**2
Iy_tot=sum(Iy)
Ix_tot=sum(Ix)
resposta(Ix_tot,'m^4')
