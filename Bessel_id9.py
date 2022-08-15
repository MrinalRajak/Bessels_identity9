
#Bessle's identity
#(9)

import numpy as np
from scipy.special import jn
from scipy.integrate import quad
from scipy.misc import derivative

n=int(input("Enter the n: "))
x=float(input("Enter the x: "))
LHS= jn(n+1,x)
RHS= ((2*n)/x)*jn(n,x)- jn(n-1,x)
print("LHS: ",LHS)
print("RHS: ",RHS)
