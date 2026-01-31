import numpy as np
from comparison_logic import get_selected_inter_arrays, create_cost_matrix


def get_path(cost_matrix):
    p_end = (0, 0)
    current_pt = (cost_matrix.shape[0]-1, cost_matrix.shape[1]-1)
    optimal_path = [current_pt]
    while current_pt != p_end:
        if current_pt[0] == 0:
            current_pt = (current_pt[0], current_pt[1]-1)
        elif current_pt[1] == 0:
            current_pt = (current_pt[0]-1, current_pt[1])
        else:
            values = [cost_matrix[current_pt[0]-1, current_pt[1]-1], cost_matrix[current_pt[0]-1, current_pt[1]], cost_matrix[current_pt[0], current_pt[1]-1]]
            max_idx = np.argmax(values)
            if max_idx == 0:
                current_pt = (current_pt[0]-1, current_pt[1]-1)
            elif max_idx == 1:
                current_pt = (current_pt[0]-1, current_pt[1])
            else:
                current_pt = (current_pt[0], current_pt[1]-1)
        optimal_path.append(current_pt)
    return optimal_path


def get_dynamic_time_warping_path(sorting_alg, config):
    cost_matrices = {}
    optimal_mapping = {}
    path_dict_values = {}
    for key1, value1 in sorting_alg.items():
        for key2, value2 in sorting_alg.items():
            if key1 != key2:
                ordered_key = (key1, key2)
                if (key2, key1) not in cost_matrices.keys():
                    cost_matrices[ordered_key] = create_cost_matrix(value1, value2, config)
                    path = get_path(cost_matrices[ordered_key])
                    x_vals, y_vals = zip(*path)
                    path_dict_values[ordered_key] = x_vals, y_vals
                    optimal_mapping[ordered_key] = get_selected_inter_arrays(x_vals, y_vals, value1, value2)
    return optimal_mapping, cost_matrices, path_dict_values

