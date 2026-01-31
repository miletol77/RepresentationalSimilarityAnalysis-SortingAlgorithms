import logging
import os
import numpy as np

from datetime import datetime

from run_config import RunConfig
from sort_arrays import sort_arrays
from concurrent.futures import ProcessPoolExecutor, as_completed
from linear_sum_assignment import get_linear_sum_assignment_indexes
from dynamic_time_warping import get_dynamic_time_warping_path
from create_rdm import get_rdm_algorithms
from perform_rsa import create_rsa_matrix
from plotting import plot_rsa_score, plot_cost_rows_rdm
from results import plot_results_from_file

AMOUNT_ARRAYS = 9

def get_optimal_mapping(algorithm_results, config):
    if config.dynamic_time_warping:
        return get_dynamic_time_warping_path(algorithm_results, config)
    return get_linear_sum_assignment_indexes(algorithm_results, config)


def process_iteration(config):
    sorting_results = sort_arrays(config.size_array, AMOUNT_ARRAYS, config.distinct_arrays)
    alg_names = list(sorting_results.keys())
    opt_rdm, cost_matrices, rows_cols = get_optimal_mapping(sorting_results, config)
    rdms = get_rdm_algorithms(opt_rdm, config)
    rsa_matrix, rsa_scores = create_rsa_matrix(rdms, alg_names)
    if config.plot_rdm: plot_cost_rows_rdm(rdms, cost_matrices, rows_cols, config)
    if config.plot_rsa_matrix: plot_rsa_score(rsa_matrix, alg_names, config)
    return rsa_scores


def run_simulation(config: RunConfig):
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    if config.dynamic_time_warping:
        log_filename = os.path.join(log_dir, f"dtw_{timestamp}.log")
    else:
        log_filename = os.path.join(log_dir, f"lsa_{timestamp}.log")

    logger = logging.getLogger(f"simulation_{timestamp}")
    logger.setLevel(logging.INFO)

    handler = logging.FileHandler(log_filename)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.propagate = False

    setting = f"Comparing Using {config.get_method()}: Size Arrays {config.size_array} Distinct Arrays: {config.distinct_arrays} Iterations {config.num_iterations} Using {config.get_metric()}"
    print(setting)
    logger.info(setting)

    rsa_mat_iter = {}
    num_threads = os.cpu_count()
    with ProcessPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(process_iteration, config) for _ in range(config.num_iterations)]
        results = [future.result() for future in as_completed(futures)]
        for rsa_scores in results:
            for key, value in rsa_scores.items():
                if rsa_mat_iter.get(key) is None:
                    rsa_mat_iter[key] = [value]
                else:
                    rsa_mat_iter[key].append(value)

    var_arr = []
    for k, v in rsa_mat_iter.items():
        mean = np.mean(v)
        var = np.var(v, mean=mean)
        var_arr.append(var)
        logger.info("Key: " + k[0] + " " + k[1] + " MEAN: " + str(mean) + " VARIANCE: " + str(var))

    logger.info("Mean Variance: " + str(np.mean(var_arr)))
    plot_results_from_file(log_filename, config)

    handler.close()
    logger.removeHandler(handler)

