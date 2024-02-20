AO=(2**2+1.5**2+c**2)**0.5
cos_AO_x=2/AO
cos_AO_y=1.5/AO
cos_AO_z=c/AO

AC=(2**2+(1.5+a)**2+c**2)**0.5
cos_AC_x=2/AC
cos_AC_y=(1.5+a)/AC
cos_AC_z=c/AC

AB=((2+b)**2+(1.5+a)**2+c**2)**0.5
cos_AB_x=(b+2)/AB
cos_AB_y=(1.5+a)/AB
cos_AB_z=c/AB

g=9.81
modFAO,modFAC,modFAB=sy.symbols(r'|F_{AO}| |F_{AC}| |F_{AB}|')
P=m*g*vector(0,0,-1)
FAO=modFAO*vector(+cos_AO_x,-cos_AO_y,+cos_AO_z)
FAC=modFAC*vector(-cos_AC_x,+cos_AC_y,-cos_AC_z)
FAB=modFAB*vector(-cos_AB_x,+cos_AB_y,-cos_AB_z)
eq=P+FAO+FAC+FAB
eq1=eq.dot(i)
eq2=eq.dot(j)
eq3=eq.dot(k)

result=sy.solve([eq1,eq2,eq3],[modFAO,modFAC,modFAB])
modFAO=result[modFAO]
modFAB=result[modFAB]
modFAC=result[modFAC]
resposta(modFAB,'N')
