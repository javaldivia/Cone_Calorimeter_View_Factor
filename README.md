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

Radiative heat transfer plays a crucial role in fire testing, particularly in cone calorimeter experiments conducted under [**ISO 5660**](https://www.iso.org/standard/57957.html) and [**ASTM E1354**](https://www.astm.org/e1354-23.html). These standards assume a uniform irradiance distribution over the specimen surface, but in practice, spatial variations can occur due to geometric and optical factors.  

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

The figure below illustrates the experimental setup and dimensions for the cone calorimeter heater, showing two idealized geometries: a **helical coil (HC)** arrangement (left) and a **truncated cone (TC)** (right). The constants are defined as $R_1 = R_2 = 40$ mm and $H = 65$ mm, following the [ISO 5660](https://www.iso.org/standard/57957.html) standard. The key parameters used in the calculations are also shown.  

![Schematic of the experimental setup](images/Cone_ISOM.png)  
*Figure 1: Schematic of the experimental setup and dimensions for the cone calorimeter heater (not to scale), illustrating two idealized geometries: a helical coil arrangement (left) and a truncated cone (right).*  

### View Factor Computation  

This repository contains four Python scripts for computing the **view factor (VF)** in the cone heater setup:  

- **`VF_dA_to_HC.py`** – Computes the view factor from a **differential element** (disk of diameter $p$) to the **helical coil (HC)** representation of the heater.  
- **`VF_dA_to_TC.py`** – Computes the view factor from a **differential element** (disk of diameter $p$) to the **truncated cone (TC)** representation of the heater.  
- **`VF_sample_to_HC.py`** – Computes the view factor from a **square sample** of side length $p$ to the **helical coil (HC)**.  
- **`VF_sample_to_TC.py`** – Computes the view factor from a **square sample** of side length $p$ to the **truncated cone (TC)**.  

### Parameters  

- **For `VF_dA_to_HC.py` and `VF_dA_to_TC.py` (Differential Element, $dA$ to HC or TC)**:  
  - $h, k$: $(x,y)$ coordinates of the center of the differential element. In Fig. 1: $(h,k)=(x_g,y_g)$.
  - $d$: Vertical distance from the cone heater to the differential element. **Note that you should account for the 5 mm thickness of the plate, $d_2$, in the calculation so that $d=d_1+d_2$** (see Fig. 1). For example, at the standard distance of $d_1=25$ mm, in the view factor calculation: $d=d_1+d_2 =30$ mm. 
  - $p$: Diameter of the differential element (in mm).

- **For `VF_sample_to_HC.py` and `VF_sample_to_TC.py` (Sample to HC or TC)**:  
  - $d$: Vertical distance from the cone heater to the sample ($d = d_1$).  
  - $p$: Side length of the square sample (in mm).  

These parameters, as illustrated in the schematic, define the spatial configuration for computing the view factors.  

## Mathematical formulation

### Radiative heat flux
The incident radiation to the target, represented by the heat flux gauge sensor area and denoted as $`\dot{q}_{inc,g}''`$, is related to the power emitted from the cone heater, $\dot{q}_{emi,c}$, by the following expression:
```math
\dot{q}_{emi,c}\,F_{c\rightarrow {g}}=A_g\,\dot{q}_{inc,g}''
```
Here, $`F_{c\rightarrow {g}}`$ is the view factor from the cone heater to the gauge's sensor. By applying the reciprocity rule of view factors, $`A_{c}F_{c\rightarrow{g}}=A_{g}F_{g\rightarrow{c}}`$, the previous equation can be rearranged to express $`\dot{q}''_{inc,g}`$:
```math
\dot{q}^{\prime\prime}_{inc,g}=F_{g\rightarrow{c}}\dot{q}^{\prime\prime}_{emi,c}=F_{g\rightarrow{c}}\varepsilon_c \sigma T_c^{4}
```
In this equation, $`F_{g \rightarrow{c}}`$ is the view factor from the gauge's sensor ($g$) to the cone heater ($c$), while $\varepsilon_c$ denotes the emissivity of the cone heater surface, $\sigma$ is the Stefan-Boltzmann constant, and $T_c$ is the temperature of the cone heater. 

