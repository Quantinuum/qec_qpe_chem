# Copyright 2025 Quantinuum (www.quantinuum.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# %%
import json
import numpy as np
from matplotlib import rcParams
from scipy.optimize import curve_fit
from typing import NamedTuple
import matplotlib.pyplot as plt

rcParams["font.size"] = 12

# Parameter.
formats = ["o", "^", "v", "s", "<", ">", "p", "D", "*", "X"]


class Property(NamedTuple):
    color: str
    label: str


LSDATA = [
    ("pft_hardware", Property("red", "PFT")),
    ("exp_hardware", Property("green", "Exp")),
    ("dir_hardware", Property("blue", "Dir")),
    ("phys_hardware", Property("gray", "Physical")),
]


def fun(x, error_rate, param):
    q = np.exp(-error_rate * x - param)
    y = (1 + q) / 2.0
    return y


for i, (target, prop) in enumerate(LSDATA):
    with open(f"{target}/_benchmark_result.json") as f:
        benchmark_result = json.load(f)
    ks = [3, 6, 9, 12]
    p0 = np.array(benchmark_result["p0"])
    # Use the stored circuit-wise standard error.
    se = np.asarray(benchmark_result["p0_unc"])
    popt, pcov = curve_fit(
        fun,
        ks,
        p0,
        sigma=se,
        p0=[0.0, 0.0],
    )
    for popti, pcovi in zip(popt, np.diag(pcov)**0.5):
        print(f"error_rate = {popti:9.5f} +/- {pcovi:9.5f}")
    plt.errorbar(
        ks, [min(v, 1.0) for v in 2 * (1 - p0)], yerr=2 * se,
        capsize=5,
        fmt=formats[i],
        markersize=6,
        ecolor=prop.color,
        markeredgecolor=prop.color,
        color='w',
        alpha=0.75,
        label=prop.label,
    )
    xfit = np.linspace(0, ks[-1]+50, 100)
    xfit = np.arange(0, ks[-1]+50, 1, dtype=float)
    yfit = 2 * (1 - fun(xfit, *popt))
    plt.plot(xfit, yfit, "-", color=prop.color, alpha=0.6)
plt.xlabel(r"$k$")
plt.grid()
plt.ylabel(r"$q$")
plt.legend(fontsize=10)
plt.xlim(0.0, 14)
plt.ylim(-0.05, 1.1)
# plt.show()
plt.savefig("_fig_calibration_compare.pdf", dpi=300)
