from scipy import stats
from numpy import corrcoef

def calculate_correlation(array1, array2):
    return 1 - corrcoef(array1, array2)[0, 1]

def calculate_spearman_rank_coefficient(a, b):
    return abs(stats.spearmanr(a, b).statistic)

def calculate_kendall_tau_coefficient(a, b):
    return abs(stats.kendalltau(a, b).statistic)
