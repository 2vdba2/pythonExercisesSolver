x=sy.symbols('x')
F=w*a
FRAx=0
FRCy=(MB+a*F/2)/(2*a)
FRAy=-FRCy+F 
Vc1=FRAy-w*x
Mf1=sy.integrate(Vc1,x)
Vc2=Vc1.subs(x,a)
Mf2=Mf1.subs(x,a)+MB+sy.integrate(Vc2,(x,a,x))
def Vc(xx,Vc1,Vc2):
    x=sy.symbols('x')
    try:
        n=len(xx)
    except:
        xx=np.array([xx])
        n=1
    V=np.zeros(n)
    for i in range(n):
        if(0<=xx[i]<a):
            V[i]= Vc1.subs(x,xx[i])
        elif(a<=xx[i]<2*a):
            V[i]=  Vc2
        else:
            V[i]= 0
    return V
def Mf(xx,Mf1,Mf2):
    x=sy.symbols('x')
    try:
        n=len(xx)
    except:
        xx=np.array([xx])
        n=1
    M=np.zeros(n)
    for i in range(n):
        if(0<=xx[i]<a):
            M[i]=Mf1.subs(x,xx[i])
        elif(a<=xx[i]<2*a):
            M[i]=Mf2.subs(x,xx[i])
        else:
            M[i]= 0
    return M
Mf_Value=Mf(xvalue,Mf1,Mf2)[0]
Vc_value=Vc(xvalue,Vc1,Vc2)[0]    
resposta(Mf(xvalue,Mf1,Mf2)[0],'kN*m')
