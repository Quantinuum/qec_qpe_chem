# Figure data and scripts

This directory contains processed experimental data and scripts for reproducing the calibration and information theory QPE figures in the [paper](../README.md).

## Calibration

`calibration/` contains benchmark results for the physical, Dir, Exp, and PFT setups, including PFT results without QEC. Each `_benchmark_result.json` records `p0`, its uncertainty `p0_unc`, and `n_shots` for Trotter step counts `k = 3, 6, 9, 12`. The scripts generate:

- `_fig_calibration.pdf`: PFT results with and without QEC.
- `_fig_calibration_compare.pdf`: comparison of the physical, Dir, Exp, and PFT setups.

## Information theory QPE

`qpe/qpe_data.json` contains aligned arrays of `k`, `beta`, and measurement outcomes for 2,186 shots. The Makefile runs `_gen_data.py` for the first 100, 500, 1,000, and 2,186 shots, then runs `_plot.py` to generate `_fig_iqpe.pdf`. The intermediate `data_*.txt` files and PDFs are generated outputs.

## Reproduce the figures

From the repository root, install the project as described in the [main README](../README.md), then run:

```sh
uv run make -C data/calibration
uv run make -C data/qpe
```

The Makefiles expect to run from their own directories; `make -C` handles that. To remove generated files, run `uv run make -C data/calibration clean` or `uv run make -C data/qpe clean`.
