import numpy as np
from numpy import zeros, tril

from comparison_logic import assemble_rsa_matrix
from comparison_metrics import calculate_correlation


def calculate_dissimilarity(rdm_dict):
    rsa_scores = {}
    for key, value in rdm_dict.items():
        corr = calculate_correlation(tril(value[0], k=-1).flatten(), tril(value[1], k=-1).flatten())
        rsa_scores[key] = corr
    return rsa_scores


def create_rsa_matrix(rdms, algorithm_name):
    rsa_scores = calculate_dissimilarity(rdms)
    size = len(algorithm_name)
    return assemble_rsa_matrix(rsa_scores, algorithm_name, np.ones((size, size))), rsa_scores

