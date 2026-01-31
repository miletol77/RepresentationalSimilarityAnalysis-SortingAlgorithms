from numpy import ones


def create_rdm(arr_to_compare, config):
    size = len(arr_to_compare)
    matrix = ones((size, size))
    for i in range(size):
        for j in range(size):
            if i < j:
                dist = config.calculate_distance(arr_to_compare[i], arr_to_compare[j])
                matrix[i,j] = matrix[j,i] = dist
    return matrix


def get_rdm_algorithms(optimal_mapping, config):
    rdm_dict = {}
    for key, value in optimal_mapping.items():
        rdm_dict[key] = create_rdm(value[0], config), create_rdm(value[1], config)
    return rdm_dict

