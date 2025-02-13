import numpy as np
from scipy.integrate import dblquad

## (1) View factor from a differential element, $p$, to the cone heater: Helical coil (HC).
def VF_dA_to_HC(h, k, d, p):
    # Constants
    R1 = 40
    R2 = 40
    H  = 65

    # Define the integral functions
    def f1(u, v):
        return (1/(np.pi**2*p**2)) * np.log(
            (0.5*p*np.cos(u)+h-(-R1-R2+R2*v/(19*np.pi))*np.cos(v))**2 +
            (0.5*p*np.sin(u)+k-(-R1-R2+R2*v/(19*np.pi))*np.sin(v))**2 +
            (H*v/(19*np.pi)+d)**2  ) * (p*R2/(38*np.pi)*np.sin(v-u)+0.5*p*(-R1-R2+(R2*v)/(19*np.pi))*np.cos(v-u)) 
    
    def f2(u, v):
        return (1/(np.pi**2*p**2)) * np.log(
            (0.5*p*np.cos(u)+h-(-R1-R2+R2*v/(19*np.pi))*np.cos(v))**2 +
            (0.5*p*np.sin(u)+k-(-R1-R2+R2*v/(19*np.pi))*np.sin(v))**2 +
            (H*v/(19*np.pi)+d)**2  ) * (p*R2/(38*np.pi)*np.sin(v-u)+0.5*p*(-R1-R2+(R2*v)/(19*np.pi))*np.cos(v-u)) 
    
    def f3(u, v):
        return (1/(np.pi**2*p**2)) * np.log(
            (0.5*p*np.cos(u)+h-(np.sqrt(H**2 + R2**2)/19)*np.cos(v)+R1+18*R2/19)**2 + 
            (0.5*p*np.sin(u)+k)**2 +
            ((np.sqrt(H**2 + R2**2)/19)*np.sin(v)+H/19 + d)**2)*(p/38)*np.sqrt(H**2 + R2**2)*np.sin(u)*np.sin(v)
    
    def f4(u, v):
        return (1/(np.pi**2*p**2)) * np.log(
            (0.5*p*np.cos(u)+h-(np.sqrt(H**2 + R2**2)/19)*np.cos(v)-R1-R2/19)**2 + 
            (0.5*p*np.sin(u)+k)**2 +
            ((np.sqrt(H**2 + R2**2)/19)*np.sin(v)+18*H/19+d)**2)*(p/38)*np.sqrt(H**2 + R2**2)*np.sin(v)*np.sin(u)
    
    # Compute the view factors
    VF = (dblquad(f1, 17*np.pi, 0, 0, 2*np.pi)[0] +
          dblquad(f2, 2*np.pi, 19*np.pi, 0, 2*np.pi)[0] +
          dblquad(f3, np.arctan(H/R2) - np.pi, np.arctan(H/R2), 0, 2*np.pi)[0] +
          dblquad(f4, np.pi - np.arctan(H/R2), 2*np.pi - np.arctan(H/R2), 0, 2*np.pi)[0])
    
    return VF

## (2) View factor from a differential element, $p$, to the cone heater: Truncated cone (TC).
def VF_dA_to_TC(h,k,d,p):
    # Constants
    R1 = 40
    R2 = 40
    H = 65
    
 #contour integrals
    
    f1 = lambda u, v: (1/(np.pi*np.pi*p**2))*np.log(
        (0.5*p*np.cos(u)+h-(R1+R2)*np.cos(v))**2 +
        (0.5*p*np.sin(u)+k-(R1+R2)*np.sin(v))**2+
  (d)**2)*(0.5*p*(R1+R2)*np.cos(u-v)) 
    
    f2 = lambda u, v: (1/(np.pi*np.pi*p**2))*np.log(
        (0.5*p*np.cos(u)+h-R1*np.cos(v))**2 +
        (0.5*p*np.sin(u)+k-R1*np.sin(v))**2+
  (H+d)**2)*(0.5*p*R1*np.cos(u-v)) 
    
    
    VF = dblquad(f1, 2*np.pi, 0, 0, 2*np.pi)[0] + dblquad(f2, 0, 2*np.pi, 0, 2*np.pi)[0] 
    error = dblquad(f1, 2*np.pi, 0, 0, 2*np.pi)[1] + dblquad(f2, 0, 2*np.pi, 0, 2*np.pi)[1]  
    
    return VF

## (3) View factor from square sample, $s$, of side $p$, to the cone heater: Helical coil (HC)
def VF_sample_HC(p, d):
    R1 = 40  # radial distance
    R2 = 40  # radial distance
    H  = 65   # cone-heater height
    
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

    
    VF=(dblquad(I1,17*np.pi,0,0,1)[0] + dblquad(I2,2*np.pi,19*np.pi,0,1)[0] + dblquad(I3,np.arctan(H/R2)-np.pi,np.arctan(H/R2),0,1)[0] + dblquad(I4,np.pi-np.arctan(H/R2),2*np.pi-np.arctan(H/R2),0,1)[0] + dblquad(I5,17*np.pi,0,0,1)[0]
    +dblquad(I6,2*np.pi,19*np.pi,0,1)[0] + dblquad(I7,17*np.pi,0,0,1)[0] + dblquad(I8,2*np.pi,19*np.pi,0,1)[0] + dblquad(I9,np.arctan(H/R2)-np.pi,np.arctan(H/R2),0,1)[0] + dblquad(I10,np.pi-np.arctan(H/R2),2*np.pi-np.arctan(H/R2),0,1)[0] 
    + dblquad(I11,17*np.pi,0,0,1)[0] + dblquad(I12,2*np.pi,19*np.pi,0,1)[0])
    
    return VF

## (4) View factor from square sample, $s$, of side $p$, to the cone heater: Truncated cone (TC)
def VF_sample_TC(p, d):
    R1 = 40  # radial distance
    R2 = 40  # radial distance
    H  = 65   # cone-heater height

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
