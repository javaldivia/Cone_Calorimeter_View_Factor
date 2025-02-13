# Cone Calorimeter View Factor

These set of codes calculates the view factor from a target (differential element or a sample surface) to the cone calorimeter heater. 

## Analysis of Radiative Heat Transfer in Cone Heater Experiments

This repository provides Python scripts for analyzing radiative heat transfer in cone heater experiments, focusing on view factors and irradiance distribution. The code is based on the methodologies detailed in our paper:

> Title: [Investigating radiation heat transfer from the cone calorimeter heater: a new view factor model and uncertainty quantification]  
> Authors: [Pablo E. Pinto, Jorge Valdivia, Abhinandan Singh, Xiuqi Xi, Juan Cuevas, James L. Urban] 
> Journal: [International Journal of Heat and Mass Transfer], [2025].  
> DOI: [https://doi.org/10.2139/ssrn.5085144]

The scripts implement calculations related to view factors, spatial irradiance variations, and experimental data processing, enabling accurate assessment of heat flux distributions in standardized fire testing scenarios. These computations are particularly relevant to tests conducted under ISO 5660 and ASTM E1354, where uniformity of incident radiation is often assumed but requires further scrutiny.

For a comprehensive discussion of the theoretical framework and experimental validation, please refer to the full paper. This repository serves as a practical implementation of the described methodologies.

## Background  

Radiative heat transfer plays a crucial role in fire testing, particularly in cone calorimeter experiments conducted under **ISO 5660** and **ASTM E1354**. These standards assume a uniform irradiance distribution over the specimen surface, but in practice, spatial variations can occur due to geometric and optical factors.  

A **cone heater** is commonly used to provide a controlled heat flux to a sample, simulating fire exposure conditions. The distribution of irradiance on the specimen is influenced by the **view factor**, which accounts for the geometric relationship between the heater and the sample. Deviations from uniformity can lead to inaccuracies in heat flux measurements, material degradation analysis, and fire modeling efforts.  

This repository provides tools for computing **view factors** and analyzing the spatial distribution of irradiance in cone heater setups. The implemented algorithms enable precise quantification of heat flux variations, supporting a more rigorous interpretation of experimental results.  

For a detailed theoretical discussion, derivations, and experimental validation, refer to the associated publication. 

## Installation & Usage  

### Requirements  
This code requires Python 3 and the following dependencies:  

- `numpy`  
- `scipy` (for numerical integration)  

Ensure these are installed using:  

```bash
pip install numpy scipy
```
## Schematic Representation & Description of Scripts  

The figure below illustrates the experimental setup and dimensions for the cone calorimeter heater, showing two idealized geometries: a **helical coil (HC)** arrangement (left) and a **truncated cone (TC)** (right). The constants are defined as $R_1 = R_2 = 40$ mm and $H = 65$ mm, following the ISO 5660 standard. The key parameters used in the calculations are also shown.  

![Schematic of the experimental setup](images/Cone_ISOM.png)  
*Figure: Schematic of the experimental setup and dimensions for the cone calorimeter heater (not to scale), illustrating two idealized geometries: a helical coil arrangement (left) and a truncated cone (right).*  

### View Factor Computation  

This repository contains four Python scripts for computing the **view factor (VF)** in the cone heater setup:  

- **`VF_dA_to_HC.py`** – Computes the view factor from a **differential element** (disk of diameter $p$) to the **helical coil (HC)** representation of the heater.  
- **`VF_dA_to_TC.py`** – Computes the view factor from a **differential element** (disk of diameter $p$) to the **truncated cone (TC)** representation of the heater.  
- **`VF_sample_to_HC.py`** – Computes the view factor from a **square sample** of side length $p$ to the **helical coil (HC)**.  
- **`VF_sample_to_TC.py`** – Computes the view factor from a **square sample** of side length $p$ to the **truncated cone (TC)**.  

### Parameters  

- **For `VF_dA_to_HC.py` and `VF_dA_to_TC.py` (Differential Element to HC or TC)**:  
  - $h, k$: $(x,y)$ coordinates of the center of the differential element.  
  - $d$: Vertical distance from the cone heater base plate to the target ($d = d_1$).  
  - $p$: Diameter of the differential element (in mm).  

- **For `VF_sample_to_HC.py` and `VF_sample_to_TC.py` (Sample to HC or TC)**:  
  - $d$: Vertical distance from the cone heater base plate to the target ($d = d_1$).  
  - $p$: Side length of the square sample (in mm).  

These parameters, as illustrated in the schematic, define the spatial configuration for computing the view factors.  


