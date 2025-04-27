# Cone Calorimeter View Factor

This repository provides Python codes to calculate view factors from a differential element or sample surface to a cone calorimeter heater. These computations support improved assessment of spatial irradiance distributions in fire testing experiments.

If you find this code useful, please cite our work:

[![Published Article](https://img.shields.io/badge/Article-International%20Journal%20of%20Heat%20and%20Mass%20Transfer-blue)](https://doi.org/10.1016/j.ijheatmasstransfer.2025.126976)

---

## Repository Version

- **Version**: 1.0.0  
- **Release Date**: March 25, 2025  
- **Changelog**: Initial release  

---

## About the Paper

> **Title:** Investigating radiation heat transfer from the cone calorimeter heater: A new view factor model and uncertainty quantification  
> **Authors:**  
> **Pablo E. Pinto** [![ORCID](https://img.shields.io/badge/ORCID-0009--0005--2274--9746-a6ce39?logo=orcid&style=flat-square)](https://orcid.org/0009-0005-2274-9746) <br>  
> **Jorge Valdivia** [![ORCID](https://img.shields.io/badge/ORCID-0009--0003--4251--1108-a6ce39?logo=orcid&style=flat-square)](https://orcid.org/0009-0003-4251-1108) <br>  
> **Abhinandan Singh** [![ORCID](https://img.shields.io/badge/ORCID-0000--0002--7995--950X-a6ce39?logo=orcid&style=flat-square)](https://orcid.org/0000-0002-7995-950X) <br>  
> **Xiuqi Xi** [![ORCID](https://img.shields.io/badge/ORCID-0000--0003--3245--232X-a6ce39?logo=orcid&style=flat-square)](https://orcid.org/0000-0003-3245-232X) <br>  
> **Juan Cuevas** [![ORCID](https://img.shields.io/badge/ORCID-0000--0002--1504--5530-a6ce39?logo=orcid&style=flat-square)](https://orcid.org/0000-0002-1504-5530) <br>  
> **James L. Urban** [![ORCID](https://img.shields.io/badge/ORCID-0000--0002--2476--8212-a6ce39?logo=orcid&style=flat-square)](https://orcid.org/0000-0002-2476-8212) <br>  
> **Journal:** *International Journal of Heat and Mass Transfer* (2025)  
> **DOI:** [https://doi.org/10.1016/j.ijheatmasstransfer.2025.126976](https://doi.org/10.1016/j.ijheatmasstransfer.2025.126976)

A **preprint manuscript** is included in this repository under the filename **Cone_Heater_Paper.pdf**.

The scripts implement calculations related to view factors and spatial irradiance variations, enabling accurate assessment of heat flux distributions in standardized fire testing scenarios. These computations are particularly relevant to tests conducted under ISO 5660 and ASTM E1354, where uniformity of incident radiation is often assumed but requires further scrutiny.

---

## Analysis of Radiative Heat Transfer in Cone Heater Experiments

This repository provides Python scripts for analyzing radiative heat transfer in cone heater experiments, focusing on view factors and irradiance distribution. The code is based on the methodologies detailed in our paper:

> **Title:** [Investigating radiation heat transfer from the cone calorimeter heater: a new view factor model and uncertainty quantification]  
> **Authors:** [Pablo E. Pinto](https://orcid.org/0009-0005-2274-9746), [Jorge Valdivia](https://orcid.org/0009-0003-4251-1108), [Abhinandan Singh](https://orcid.org/0000-0002-7995-950X), [Xiuqi Xi](https://orcid.org/0000-0003-3245-232X), [Juan Cuevas](https://orcid.org/0000-0002-1504-5530), [James L. Urban](https://orcid.org/0000-0002-2476-8212)  
> **Journal:** *International Journal of Heat and Mass Transfer*, in press, [2025].  
> **DOI:** [https://doi.org/10.2139/ssrn.5085144]


The **preprint manuscript** is available in this repository under the filename **Cone_Heater_Paper.pdf**.

The scripts implement calculations related to view factors, spatial irradiance variations, and experimental data processing, enabling accurate assessment of heat flux distributions in standardized fire testing scenarios. These computations are particularly relevant to tests conducted under ISO 5660 and ASTM E1354, where uniformity of incident radiation is often assumed but requires further scrutiny.

For a comprehensive discussion of the theoretical framework and experimental validation, please refer to the full paper. This repository serves as a practical implementation of the described methodologies.

---

## Background

Cone calorimeter experiments conducted under [**ISO 5660**](https://www.iso.org/standard/57957.html) and [**ASTM E1354**](https://www.astm.org/e1354-23.html) standards assume a uniform irradiance distribution over the sample surface. However, spatial variations due to heater geometry and temperature non-uniformity can impact experimental results.

Accurate quantification of these effects requires computation of the **view factor** between the cone heater and a target (sensor or specimen surface). This repository provides tools to model these view factors for both **truncated cone (TC)** and **helical coil (HC)** geometries.

For detailed theoretical derivations and validation with experimental data, please refer to the full paper linked above.

---

## Installation

### Requirements

- `numpy`
- `scipy`

Install with:
```python
pip install numpy scipy
```

---

## Schematic Representation

The figure below illustrates the idealized geometries of the cone heater analyzed:

![Schematic of the experimental setup](images/Cone_ISOM_HC_TC.png)  
*Figure 1: Schematics of the cone calorimeter heater: Helical Coil (HC, left) and Truncated Cone (TC, right).*

Key dimensions:
- $R_1 = R_2 = 40$ mm
- $H = 65$ mm

---

## Structure of the Codes

Four Python scripts are provided for calculating view factors:

| Script | Description |
|:-------|:------------|
| `VF_dA_to_HC.py` | View factor from a differential disk element to a **Helical Coil (HC)** |
| `VF_dA_to_TC.py` | View factor from a differential disk element to a **Truncated Cone (TC)** |
| `VF_sample_to_HC.py` | View factor from a square sample to a **Helical Coil (HC)** |
| `VF_sample_to_TC.py` | View factor from a square sample to a **Truncated Cone (TC)** |

---

## Input Parameters

**Differential Element Scripts (`VF_dA_to_HC.py`, `VF_dA_to_TC.py`):**

- h, k: (x, y) center coordinates of the disk (in mm)
- d: Vertical distance from cone heater to disk (account for plate thickness)
- p: Disk diameter (in mm)

**Sample Scripts (`VF_sample_to_HC.py`, `VF_sample_to_TC.py`):**

- d: Vertical distance from cone heater to sample (in mm)
- p: Side length of square sample (in mm)

---

## Example Usage

View factor from a differential element to HC:
```python
d1 = 25  
d2 = 5  
d = d1 + d2  
p = 10**(-5)  
h, k = 0, 0

VF = VF_dA_to_HC(h, k, d, p)  
print(f'The View Factor is: {VF:.4f}')
```
Expected Output:
```pgsql
The View Factor is: 0.6690
```
---

View factor from a square sample to HC:
```python
d1 = 25  
d2 = 5  
d = d1 + d2  
p = 100

VF = VF_sample_HC(d, p)  
print(f'The View Factor is: {VF:.4f}')
```
Expected Output:
```pgsql
The View Factor is: 0.6216
```
---

## Mathematical Formulation


### Radiative heat flux
The incident radiation to the target, represented by the heat flux gauge sensor area and denoted as $`\dot{q}_{inc,g}^{\prime\prime}`$, is related to the power emitted from the cone heater, $\dot{q}_{emi,c}$, by the following expression:
```math
\dot{q}_{emi,c}\,F_{c\rightarrow {g}}=A_g\,\dot{q}_{inc,g}^{\prime\prime}
```

Here, $`F_{c\rightarrow {g}}`$ is the view factor from the cone heater to the gauge's sensor. By applying the reciprocity rule of view factors, $`A_{c}F_{c\rightarrow{g}}=A_{g}F_{g\rightarrow{c}}`$, the previous equation can be rearranged to express $`\dot{q}^{\prime\prime}_{inc,g}`$:
```math
\dot{q}^{\prime\prime}_{inc,g}=F_{g\rightarrow{c}}\dot{q}^{\prime\prime}_{emi,c}=F_{g\rightarrow{c}}\varepsilon_c \sigma T_c^{4}
```

In this equation, $`F_{g \rightarrow{c}}`$ is the view factor from the gauge's sensor ($g$) to the cone heater ($c$), while $\varepsilon_c$ denotes the emissivity of the cone heater surface, $\sigma$ is the Stefan-Boltzmann constant, and $T_c$ is the temperature of the cone heater. 

### View factor definition
The view factor between two finite surfaces, $A_{i}$ and $A_{j}$, can be calculated mathematically from their contours $`\Gamma_{i}`$ and $`\Gamma_{j}`$, respectively, by applying Stokes' theorem twice to the view factor definition (given by the surface integrals):
```math
F_{{i}\rightarrow{{j}}}=\dfrac{1}{2\pi A_{i}}\oint_{\Gamma_{j}}\oint_{\Gamma_{i}}\ln(R_{ij})\,d\boldsymbol{r}_{i}d\boldsymbol{r}_{j}
```

Here, $`R_{ij}`$ represents the Euclidean distance between the contours defined by the positions $`\boldsymbol{r}_{i}`$ and $`\boldsymbol{r}_{j}`$, respectively. This contour methodology is utilized to determine the view factor between the cone heater and targets (e.g., radiometer or small patch of a sample surface) positioned at various locations from the cone heater.

This work focuses on calculating the view factor between a differential element, $dA$, a square sample of side length $L$, or a heat flux gauge sensor (disk) and the cone calorimeter heater. For a detailed derivation of the model, the reader is encouraged to refer to the paper.

---

## License

This repository is provided under a permissive license for academic and research purposes. Please cite our article if you use these codes.