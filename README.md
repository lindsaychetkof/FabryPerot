# Fabry-Pérot Interferometer for Quantum Tweezer Optimization

## Overview
This project focuses on the **design, simulation, and implementation** of a **Fabry-Pérot interferometer** to optimize beam quality in a 399 nm collimated laser system for **quantum tweezer trapping**.

I built and tested the system as part of my research with the **Loh Lab at the Duke Quantum Center**, where we work on developing next-generation cold atom arrays for quantum computing and simulation.

---

## Goals
- Improve **beam mode quality and alignment** for a 399 nm collimated laser used in quantum tweezer traps
- **Mode match** the input beam to a curved mirror with 10 cm radius of curvature
- Integrate optical components into a functioning **cold-atom tweezer system**

---

## Technical Summary

| Component                  | Detail |
|---------------------------|--------|
| Wavelength                | 399 nm |
| Beam Waist (Initial)      | 0.6 mm |
| Mirror Curvature          | 10 cm radius |
| Interferometer Type       | Fabry-Pérot (two-mirror cavity) |
| Alignment Technique       | Mode matching via ray matrix analysis (ABCD formalism) |
| Target Outcome            | Optimal beam confinement and minimal crosstalk in cold-atom traps |

---

## What’s in This Repo

| File/Folder               | Description |
|--------------------------|-------------|
| `/comsol/`               | Field simulation files and screenshots (if shareable) |
| `/python/`               | Scripts for Gaussian beam propagation, mode matching, and ABCD matrix simulation |
| `README.md`              | This file |

---

## Key Results
- Reduced off-axis beam distortion across trap array
- Achieved effective mode matching to enhance interferometer finesse and focus
- Physically built system
