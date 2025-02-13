# Copyright (c) 2025 Jorge A. Valdivia, Pablo E. Pinto, Abhinandan Sing, Xiuqi Xi, Juan Cuevas and James L. Urban
# Licensed under the MIT License (see LICENSE file for details)

import numpy as np
from scipy.integrate import dblquad

# View factor from square sample of side 'p', to the cone heater (truncated cone - TC)
# Parameters:
# d: vertical distance (d1) from the lower of the cone heater base plate to the target (in mm)
# p: size of the square sample (in mm)

def VF_sample_TC(d, p):
    # Constants (Refer to ISO 5660-1 or ASTM E1354)
    R1 = 40  # radial distance
    R2 = 40  # radial distance
    H  = 65  # cone-heater height

    I1 =lambda u,v:( 1/(4*np.pi* p**2))*np.log((0.5*p-p*u-(R1+R2)*np.cos(v))**2 + (0.5*p-(R1+R2)*np.sin(v))**2 + (d)**2 )*p*(R1+R2)*np.sin(v)
    I2 =lambda u,v:( 1/(4*np.pi* p**2))*np.log((0.5*p-p*u-R1*np.cos(v))**2 + (0.5*p-R1*np.sin(v))**2 + (H+d)**2 )*p*(R1)*np.sin(v)
    I3 =lambda u,v:( -1/(4*np.pi* p**2))*np.log((0.5*p+(R1+R2)*np.cos(v))**2 + (0.5*p-p*u-(R1+R2)*np.sin(v))**2 + (d)**2 )*p*(R1+R2)*np.cos(v)
    I4 =lambda u,v:( -1/(4*np.pi* p**2))*np.log((0.5*p+R1*np.cos(v))**2 + (0.5*p-p*u-R1*np.sin(v))**2 + (H+d)**2 )*p*(R1)*np.cos(v)
    I5 =lambda u,v:( -1/(4*np.pi* p**2))*np.log((p*u-0.5*p-(R1+R2)*np.cos(v))**2 + (0.5*p+(R1+R2)*np.sin(v))**2 + (d)**2 )*p*(R1+R2)*np.sin(v)
    I6 =lambda u,v:( -1/(4*np.pi* p**2))*np.log((p*u-0.5*p-R1*np.cos(v))**2 + (0.5*p+R1*np.sin(v))**2 + (H+d)**2 )*p*(R1)*np.sin(v)
    I7 =lambda u,v:( 1/(4*np.pi* p**2))*np.log((0.5*p-(R1+R2)*np.cos(v))**2 + (p*u-0.5*p-(R1+R2)*np.sin(v))**2 + (d)**2 )*p*(R1+R2)*np.cos(v)
    I8 =lambda u,v:( 1/(4*np.pi* p**2))*np.log((0.5*p-R1*np.cos(v))**2 + (p*u-0.5*p-R1*np.sin(v))**2 + (H+d)**2 )*p*(R1)*np.cos(v)
    
    VF=(dblquad(I1,2*np.pi,0,0,1)[0] + dblquad(I2,0,2*np.pi,0,1)[0] + dblquad(I3,2*np.pi,0,0,1)[0] + dblquad(I4,0,2*np.pi,0,1)[0] + dblquad(I5,2*np.pi,0,0,1)[0]
        +dblquad(I6,0,2*np.pi,0,1)[0] + dblquad(I7,2*np.pi,0,0,1)[0] + dblquad(I8,0,2*np.pi,0,1)[0])

    return VF

# Example usage
d = 20
p = 100

VF = VF_sample_TC(d,p)
print(f'The View Factor is: {VF:.4f}')
