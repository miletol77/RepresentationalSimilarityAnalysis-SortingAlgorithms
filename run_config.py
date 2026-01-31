import os
import time

from dataclasses import dataclass
from comparison_metrics import calculate_spearman_rank_coefficient, calculate_kendall_tau_coefficient


@dataclass(frozen=True)
class RunConfig:
    size_array: int
    num_iterations: int
    distinct_arrays: bool
    dynamic_time_warping: bool
    kendall_tau: bool
    plot_rdm: bool
    plot_rsa_matrix: bool

    def tag(self) -> str:
        parts = [
            "KT" if self.kendall_tau else "SPR",
            "DTW" if self.dynamic_time_warping else "LSA",
            "Distinct" if self.distinct_arrays else "Equal",
            f"SizeArray{self.size_array}",
            f"Iterations{self.num_iterations}"
        ]
        return "_".join(parts)

    def filename(self, prefix, ext="png") -> str:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        return f"{prefix}_{self.tag()}_{timestamp}_pid{os.getpid()}.{ext}"

    def get_method(self):
        return "Dynamic Time Warping" if self.dynamic_time_warping else "Linear Sum Assignment"

    def get_metric(self):
        return "Kendall Tau" if self.kendall_tau else "Spearman Rank"

    def calculate_distance(self, a, b):
        return calculate_kendall_tau_coefficient(a, b) if self.kendall_tau else calculate_spearman_rank_coefficient(a, b)

