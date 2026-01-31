from numpy import zeros


def get_selected_inter_arrays(row, col, inter_arr1, inter_arr2):
    return [inter_arr1[r] for r in row], [inter_arr2[c] for c in col]


def create_cost_matrix(a, b, config):
    cost_matrix = zeros((len(a), len(b)))
    for i in range(len(a)):
        for j in range(len(b)):
            cost_matrix[i, j] = config.calculate_distance(a[i], b[j])
    return cost_matrix


def change_values(val):
    return 1 - val


def assemble_rsa_matrix(rsa_scores, algorithm_name, rsa_mat):
    for key, value in rsa_scores.items():
        key1, key2 = key
        if key1 in algorithm_name and key2 in algorithm_name:
            i, j = algorithm_name.index(key1), algorithm_name.index(key2)
            value = change_values(value)
            rsa_mat[i, j] = value
            rsa_mat[j, i] = value
    return rsa_mat

