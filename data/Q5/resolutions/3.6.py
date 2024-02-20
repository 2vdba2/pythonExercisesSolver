RGy=K/2+P/2+3/2*W+T

dJK=((3*a)**2+b**2)**0.5
FJK=(4*(T-RGy)+P+5*W)*(dJK)/(2*b)
FJKx=3*a/dJK*FJK
FJKy=b/dJK*FJK
FCB=-FJKx
FCK=FJKy+P+2*W+T-RGy
resposta(FJK,'kN')
