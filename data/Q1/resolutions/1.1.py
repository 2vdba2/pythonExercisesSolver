a,b,c,d,e, modF = sy.symbols(r"a b c d e |F|")
symbolVector = [a,b,c,d,e]
valuesVector = [va,vb,vc,vd,ve]
BC=-c*i-a*j+b*k
BCu=unit(BC)
CD=vector(-c,e,b)
CDu=unit(CD)
F=100*CDu
norm_F_BC=projectNorm(F,BC)
norm_F_BC_value=float(subValues(norm_F_BC,symbolVector,valuesVector))
resposta(norm_F_BC_value,'N')
