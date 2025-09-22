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
from typing import NamedTuple
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams["font.size"] = 12

# Chemistry data.
class ChemData(NamedTuple):
    # Basic values
    FCI_ENERGY: float = -1.13730605
    APPROX_ENERGY: float = -1.13629792
    DELTAT = 0.986620 / np.pi

    # H2 with R_HH = 1.5 A, qubit tapering with (-ZIZI, -IZIZ, IZZI).
    CZ: float = 0.7960489286466914
    CX: float = -0.1809233927385484
    CI: float = -0.3209561440881913

    # Energy and ansatz parameters for this specific condition.
    MAX_BITS: int = 5
    APPROX_PHASE: float = -APPROX_ENERGY * DELTAT
    ANSATZ_PARAM: float = [-0.08728706, -0.25]

    # Shifted values
    FCI_ENERGY_SHIFTED: float = FCI_ENERGY - CI
    APPROX_ENERGY_SHIFTED: float = APPROX_ENERGY - CI
    APPROX_PHASE_SHIFTED: float = -(APPROX_ENERGY - CI) * DELTAT



chem_data = ChemData()

ls_n_shots = [100, 500, 1000, 2186]
ls_limits = [[-170, -30], [-520, -250], [-1000, -500], [-2100, -1300]]

fig, ax = plt.subplots(
    nrows=4,
    ncols=1,
    sharex=True,
    figsize=(7, 6),
    dpi=300,
)

for i, n_shots in enumerate(ls_n_shots):
    with open(f"data_{n_shots:04d}.txt") as f:
        data = json.load(f)
    data = np.array(data)
    phi = data[:, 0]
    posterior_log = data[:, 1]

    phi2 = np.pi * phi
    phi_energy = -phi / chem_data.DELTAT

    ax[i].cla()
    ax[i].plot(phi2, posterior_log, "k-")
    ax[i].plot(
        [-np.pi * chem_data.FCI_ENERGY_SHIFTED * chem_data.DELTAT] * 2,
        [min(posterior_log), max(posterior_log) * 0.9],
        "r--",
        label=r"$-(E_{\mathrm{FCI}}-h_{3})t$",
    )
    ax[i].set_xlim(phi2[0], phi2[-1])
    ax[i].grid()
    if i == 3:
        ax[i].set_ylabel(r"$\log Q(\tilde{\phi})$", labelpad=2)
    else:
        ax[i].set_ylabel(r"$\log Q(\tilde{\phi})$", labelpad=10)
    ax[i].text(
        0.02,
        0.9,
        rf"$N_{{s}} = {n_shots}$",
        transform=ax[i].transAxes,
        fontsize=12,
        verticalalignment="top",
        bbox=dict(facecolor="white", edgecolor="none", alpha=0.7),
    )
    ax[i].set_ylim(ls_limits[i])
    # ax[i].set_title(rf"$N_{{s}} = {n_shots}$", loc="left", pad=-50)
ax[0].legend(loc="upper right", fontsize=10)
ax[3].set_xlabel(r"$\tilde{\phi}$")
plt.tight_layout()
# plt.show()

plt.savefig("_fig_iqpe.pdf", dpi=300, bbox_inches="tight")
# %%
