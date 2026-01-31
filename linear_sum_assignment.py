from scipy.optimize import linear_sum_assignment
from comparison_logic import get_selected_inter_arrays, create_cost_matrix


def perform_lsa(cost_m):
    return linear_sum_assignment(cost_matrix=cost_m, maximize=True)


def get_linear_sum_assignment_indexes(sorting_alg, config):
    cost_matrices = {}
    optimal_mapping = {}
    rows_cols = {}
    for key1, value1 in sorting_alg.items():
        for key2, value2 in sorting_alg.items():
            if key1 != key2:
                ordered_key = (key1, key2)
                if (key2, key1) not in cost_matrices.keys():
                    cost_matrices[ordered_key] = create_cost_matrix(value1, value2, config)
                    rows, cols = perform_lsa(cost_matrices[ordered_key])
                    rows_cols[ordered_key] = rows, cols
                    optimal_mapping[ordered_key] = get_selected_inter_arrays(rows, cols, value1, value2)
    return optimal_mapping, cost_matrices, rows_cols

