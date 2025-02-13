# Copyright (c) 2025 Jorge A. Valdivia, Pablo E. Pinto, Abhinandan Sing, Xiuqi Xi, Juan Cuevas and James L. Urban
# Licensed under the MIT License (see LICENSE file for details)

import numpy as np
from scipy.integrate import dblquad

# View factor from square sample of side 'p', to the cone heater (helical coil - HC)
# Parameters:
# d: vertical distance (d1) from the lower of the cone heater base plate to the target (in mm)
# p: size of the square sample (in mm)

def VF_sample_HC(d,p):
    # Constants (Refer to ISO 5660-1 or ASTM E1354)
    R1 = 40  # radial distance
    R2 = 40  # radial distance
    H  = 65  # cone-heater height
    
    I1 =lambda u,v:( 1/(4*np.pi* p**2))*np.log((p/2 -p*u-(-R1-R2+(R2*v)/(19*np.pi))*np.cos(v))**2 + (p/2-(-R1-R2 + R2*v/(19*np.pi))*np.sin(v))**2 + ((H*v/(19*np.pi))+d)**2 ) * (p*(-R1 - R2 + (R2*v)/(19*np.pi))*np.sin(v)-((p*R2)/(19*np.pi))*np.cos(v))
    I2 =lambda u,v:( 1/(4*np.pi* p**2))*np.log((p/2 -p*u-(-R1-R2+(R2*v)/(19*np.pi))*np.cos(v))**2 + (p/2-(-R1-R2+R2*v/(19*np.pi))*np.sin(v))**2 + ((H*v/(19*np.pi))+d)**2)  * (p*(-R1 - R2 + (R2*v)/(19*np.pi))*np.sin(v)-((p*R2)/(19*np.pi))*np.cos(v))
    I3 =lambda u,v:( 1/(4*np.pi* p**2))*np.log((p/2 -p*u -(np.sqrt(R2**2 + H**2)/19)*np.cos(v) + R1 + (18/19)*R2)**2 + (p/2)**2 +((np.sqrt(R2**2 + H**2)/19)*np.sin(v) + H/19 + d)**2)*(p*np.sqrt(R2**2 + H**2)/19)*np.sin(v)
    I4 =lambda u,v:( 1/(4*np.pi* p**2))*np.log((p/2 -p*u - (np.sqrt(R2**2 + H**2)/19)*np.cos(v) - R1 - (1/19)*R2)**2 + (p/2)**2 +((np.sqrt(R2**2 + H**2)/19)*np.sin(v) +(18*H)/19 + d)**2)*(p*np.sqrt(R2**2 + H**2)/19)*np.sin(v)
    I5 =lambda u,v:(-1/(4*np.pi* p**2))*np.log(((-R1 - R2 + (R2*v)/(19*np.pi))*np.cos(v) + p/2)**2+((-R1 - R2 + (R2*v)/(19*np.pi))*np.sin(v) - p/2 + p*u)**2+((H*v)/(19*np.pi) + d)**2)*(p*(-R1 - R2 + (R2*v)/(19*np.pi))*np.cos(v)+((p*R2)/(19*np.pi))*np.sin(v))
    I6 =lambda u,v:(-1/(4*np.pi* p**2))*np.log(((-R1 - R2 + (R2*v)/(19*np.pi))*np.cos(v) + p/2)**2+((-R1 - R2 + (R2*v)/(19*np.pi))*np.sin(v) - p/2 + p*u)**2+((H*v)/(19*np.pi) + d)**2)*(p*(-R1 - R2 + (R2*v)/(19*np.pi))*np.cos(v) + ((p*R2)/(19*np.pi))*np.sin(v))
    I7 =lambda u,v:( 1/(4*np.pi* p**2))*np.log((p*u -p/2 - (-R1 - R2 + (R2*v)/(19*np.pi))*np.cos(v))**2+((-R1 - R2 + (R2*v)/(19*np.pi))*np.sin(v) + p/2)**2+((H*v)/(19*np.pi) + d)**2)*(-p*(-R1 - R2 + (R2*v)/(19*np.pi))*np.sin(v) + ((p*R2)/(19*np.pi))*np.cos(v))
    I8 =lambda u,v:( 1/(4*np.pi* p**2))*np.log((p*u - p/2 - (-R1 - R2 + (R2*v)/(19*np.pi))*np.cos(v))**2+((-R1 - R2 + (R2*v)/(19*np.pi))*np.sin(v) + p/2)**2+((H*v)/(19*np.pi) + d)**2)*(-p*(-R1 - R2 + (R2*v)/(19*np.pi))*np.sin(v) + ((p*R2)/(19*np.pi))*np.cos(v))
    I9 =lambda u,v:(-1/(4*np.pi* p**2))*np.log((p*u - p/2 - (np.sqrt(R2**2 + H**2)/19)*np.cos(v) + R1 + (18/19)*R2)**2+(p/2)**2+(np.sqrt(R2**2 + H**2)/19*np.sin(v) + H/19 + d)**2)*(p*np.sqrt(R2**2 + H**2)/19)*np.sin(v)
    I10=lambda u,v:(-1/(4*np.pi* p**2))*np.log((p*u - p/2 - (np.sqrt(R2**2 + H**2)/19)*np.cos(v) -R1 - (1/19)*R2)**2+(p/2)**2+(np.sqrt(R2**2 + H**2)/19*np.sin(v) + (18*H)/19 + d)**2)*(p*np.sqrt(R2**2 + H**2)/19)*np.sin(v)
    I11=lambda u,v:( 1/(4*np.pi* p**2))*np.log(((-R1 - R2 + (R2*v)/(19*np.pi))*np.cos(v) - p/2)**2+(p*u - p/2 - (-R1 - R2 + (R2*v)/(19*np.pi))*np.sin(v))**2+((H*v)/(19*np.pi) + d)**2)*(p*(-R1 - R2 + (R2*v)/(19*np.pi))*np.cos(v) + ((p*R2)/(19*np.pi))*np.sin(v))
    I12=lambda u,v:( 1/(4*np.pi* p**2))*np.log(((-R1 - R2 + (R2*v)/(19*np.pi))*np.cos(v) - p/2)**2+(p*u - p/2 - (-R1 - R2 + (R2*v)/(19*np.pi))*np.sin(v))**2+((H*v)/(19*np.pi) + d)**2)*(p*(-R1 - R2 + (R2*v)/(19*np.pi))*np.cos(v) + ((p*R2)/(19*np.pi))*np.sin(v))

    
    VF=(dblquad(I1,17*np.pi,0,0,1)[0] +
        dblquad(I2,2*np.pi,19*np.pi,0,1)[0] +
        dblquad(I3,np.arctan(H/R2)-np.pi,np.arctan(H/R2),0,1)[0] +
        dblquad(I4,np.pi-np.arctan(H/R2),2*np.pi-np.arctan(H/R2),0,1)[0] +
        dblquad(I5,17*np.pi,0,0,1)[0] +
        dblquad(I6,2*np.pi,19*np.pi,0,1)[0] +
        dblquad(I7,17*np.pi,0,0,1)[0] +
        dblquad(I8,2*np.pi,19*np.pi,0,1)[0] +
        dblquad(I9,np.arctan(H/R2)-np.pi,np.arctan(H/R2),0,1)[0] +
        dblquad(I10,np.pi-np.arctan(H/R2),2*np.pi-np.arctan(H/R2),0,1)[0] +
        dblquad(I11,17*np.pi,0,0,1)[0] +
        dblquad(I12,2*np.pi,19*np.pi,0,1)[0]
        )
    
    return VF

# Example usage
d = 20
p = 100

VF = VF_sample_HC(d,p)
print(f'The View Factor is: {VF:.4f}')
