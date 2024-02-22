c=[np.pi*r,h,r,(r**2+h**2)**0.5]
ctot=sum(c)
dx=[0,-r,-r/2,r/2]
dy=[8/np.pi,0,0,0]
dz=[0,h/2,h,h/2]


xcm=0
ycm=0
zcm=0
for i in range(4):
    xcm+=c[i]*dx[i]/ctot
    ycm+=c[i]*dy[i]/ctot
    zcm+=c[i]*dz[i]/ctot

resposta(xcm,'m')
