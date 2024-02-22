xcm= 2*a*b**2*e/(3*(a*b*e/2 + b*d*e + b*e*(a + c + d))) + 3*b**2*d*e/(2*(a*b*e/2 + b*d*e + b*e*(a + c + d))) + b**2*e*(a + c + d)/(2*(a*b*e/2 + b*d*e + b*e*(a + c + d)))
ycm= a**2*b*e/(4*(a*b*e/2 + b*d*e + b*e*(a + c + d))) + b*d*e*(a + c + d/2)/(a*b*e/2 + b*d*e + b*e*(a + c + d)) + b*e*(a/2 + c/2 + d/2)*(a + c + d)/(a*b*e/2 + b*d*e + b*e*(a + c + d))
zcm= a*b*e**2/(6*(a*b*e/2 + b*d*e + b*e*(a + c + d))) + b*d*e**2/(2*(a*b*e/2 + b*d*e + b*e*(a + c + d))) + b*e**2*(a + c + d)/(2*(a*b*e/2 + b*d*e + b*e*(a + c + d)))
resposta(xcm,'m')
