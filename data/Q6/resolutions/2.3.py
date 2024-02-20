x=sy.symbols('x')
F=w*a/2
FRAx=0
FRBy=(MC+2/3*a*F)/a
FRAy=-FRBy+F 
Vc1=FRAy-w*x**2/(2*a)
Mf1=FRAy*x-w*x**3/(6*a)
Vc2=0
Mf2=Mf1
def Vc(xx,Vc1,Vc2):
    x=sy.symbols('x')
    if(0<=xx<a):
        return Vc1.subs(x,xx)
    elif(a<=xx<a+b):
        return Vc2
    else:
        return 0
    
def Mf(xx,Mf1,Mf2):
    x=sy.symbols('x')
    if(0<=xx<a):
        return Mf1.subs(x,xx)
    elif(a<=xx<a+b):
        return Mf2
    else:
        return 0
Mf2=Mf1.subs(x,a)
Mf_value=Mf(xx,Mf1,Mf2)
Vc_value=Vc(xx,Vc1,Vc2) 
resposta(Vc_value,'kN*m')
