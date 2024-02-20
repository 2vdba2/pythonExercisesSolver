RFy=(2*F1+3*F3+1.5*F4)/4
FEHy=RFy-F1
dEH=(2**2+1.5**2)**0.5
FEH=FEHy*dEH/1.5
FEHx=FEH*2/dEH
FGH=2*RFy/1.5
FED=-FEHx-FGH
resposta(FED,'kN')
