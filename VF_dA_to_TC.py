# Copyright (c) 2025 Jorge A. Valdivia, Pablo E. Pinto, Abhinandan Sing, Xiuqi Xi, Juan Cuevas and James L. Urban
# Licensed under the MIT License (see LICENSE file for details)

import numpy as np
from scipy.integrate import dblquad

# View factor from a differential element, dA, to the cone heater (truncated cone - TC)
# Parameters:
# h: x-coordinate location (in mm)
# k: y-coordinate location (in mm)
# d: vertical distance (d1) from the lower of the cone heater base plate to the target (in mm)
# p: differential element size (diameter, in mm)

def VF_dA_to_TC(h,k,d,p):
    # Constants (Refer to ISO 5660-1 or ASTM E1354)
    R1 = 40
    R2 = 40
    H = 65
    
    #contour integrals
    
    f1 = lambda u, v: (1/(np.pi*np.pi*p**2))*np.log(
        (0.5*p*np.cos(u)+h-(R1+R2)*np.cos(v))**2 +
        (0.5*p*np.sin(u)+k-(R1+R2)*np.sin(v))**2+(d)**2)*(0.5*p*(R1+R2)*np.cos(u-v)) 
    
    f2 = lambda u, v: (1/(np.pi*np.pi*p**2))*np.log(
        (0.5*p*np.cos(u)+h-R1*np.cos(v))**2 +
        (0.5*p*np.sin(u)+k-R1*np.sin(v))**2+(H+d)**2)*(0.5*p*R1*np.cos(u-v)) 
    
    
    VF = dblquad(f1, 2*np.pi, 0, 0, 2*np.pi)[0] + dblquad(f2, 0, 2*np.pi, 0, 2*np.pi)[0] 
    error = dblquad(f1, 2*np.pi, 0, 0, 2*np.pi)[1] + dblquad(f2, 0, 2*np.pi, 0, 2*np.pi)[1]  
    
    return VF


# Example usage
h = 0
k = 0
d = 20
p = 3.175

VF = VF_dA_to_TC(h,k,d,p)
print(f'The View Factor is: {VF:.4f}')
