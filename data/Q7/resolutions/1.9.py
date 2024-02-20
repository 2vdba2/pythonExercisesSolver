a,b,c,d,e=sy.symbols('a b c d e')
xcmi=[4*b/3,b/2,3*b/2]
ycmi=[a/2,(a+c+d)/2,a+c+d/2]
zcmi=[e/3,e/2,e/2]
Vi=[a*b*e/2,b*(a+c+d)*e,d*b*e]

xcm=0
ycm=0
zcm=0
for i in range(3):
    xcm+=xcmi[i]*Vi[i]/sum(Vi)
    ycm+=ycmi[i]*Vi[i]/sum(Vi)
    zcm+=zcmi[i]*Vi[i]/sum(Vi)
print('xcm=',xcm)
print('ycm=',ycm)
print('zcm=',zcm)
resposta(ycm,'m')
