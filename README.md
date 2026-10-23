
H2xH2 project resources
=======================

This repository contains Python tooling and processed data for reproducing the circuits, local simulations, and figures from the molecular hydrogen quantum phase estimation experiment reported in the paper:

K. Yamamoto et al., "Quantum Error-Corrected Computation of Molecular Energies", [PRX Quantum 7, 020319 (2026)](https://journals.aps.org/prxquantum/abstract/10.1103/m7j3-5sk6)

The code builds, encodes, and compiles circuits using [`pytket`](https://tket.quantinuum.com/api-docs/), with Steane code QEC and Iceberg error detection. `Rz` gates support direct and gate teleportation modes. The example notebooks use a local emulator; the original experiments ran on Quantinuum hardware. This repository does not include a Nexus job submission workflow.

`pytket` is a python module for interfacing with `TKET`, a quantum computing toolkit and optimising compiler developed by Quantinuum, and is available through `pip`. `pytket` is open source and documentation and use examples can be found at the [github repository](https://github.com/CQCL/pytket). <br>

## Disclaimer

We **stress** that the python tools available in this repository were written for the H2 on Quantinuum hardware experiment. We do not consider this code to be a prototype for running such experiments in the future. We are happy for code in this repository to be used in other work, but we do not guarantee that the code will work appropriately and any requires fixed will likely need to be made independently. While there are example notebooks and tests, API documentations and manuals are not provided.

## Installation

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then sync the project dependencies and editable `h2xh2` package from the repository root:
```
uv sync
```

Run Python commands in the project environment with `uv run`, for example `uv run python`.
