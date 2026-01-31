import matplotlib.pyplot as plt
import re
import os
import numpy as np
from scipy.stats import t

from comparison_logic import assemble_rsa_matrix, change_values

algorithm_names = ["bubble_sort", "bubble_sort_reverse", "cocktail_shaker", "selection_sort", "quick_sort", "heap_sort", "insertion_sort", "merge_sort", "radix_sort"]

def show_matrix(ax, matrix):
    im1 = ax.matshow(matrix)
    #ax.set_title(title, fontsize=15)
    ax.set_xticks(np.arange(matrix.shape[0]))
    ax.set_xticklabels(algorithm_names, rotation=-45, ha='right', fontsize=14)
    ax.set_yticks(np.arange(matrix.shape[0]))
    ax.set_yticklabels(algorithm_names, rotation=45, ha='right', fontsize=14)
    for (i, j), z in np.ndenumerate(matrix):
        ax.text(j, i, '{:0.2f}'.format(z), ha='center', va='center', fontsize=14)
    return im1


def plot_rsa_score(rsa_score, config):
    fig, axes = plt.subplots(figsize=(11, 11))
    im = show_matrix(axes, rsa_score)
    fig.colorbar(im, orientation='vertical')
    fig.suptitle("RSA Score of Sorting Algorithms", fontsize=25)

    plt.savefig(config.filename("plots/result_simulation/result_simulation"))
    plt.close(fig)


def create_matrix(rsa_dictionary):
    size = len(algorithm_names)
    return assemble_rsa_matrix(rsa_dictionary, algorithm_names, np.ones((size, size)))


def calculate_confidence_interval(first, second, mean_val, var_val, n, confidence_interval):
    crit = t.ppf(0.975, df=n - 1)
    se = np.sqrt(var_val) / np.sqrt(n)
    moe = crit * se
    print(first, second, ": ", mean_val - moe, mean_val, mean_val + moe)
    confidence_interval[(first, second)] = [mean_val, mean_val - moe, mean_val + moe]


def run_confint_plotting(filename, config):
    conf_interval = {}
    rsa_dict = {}
    n = 0
    with open(filename, 'r') as file:
        for line in file:
            match_iter = re.search(r"Iterations\s+(\d+)", line)
            if match_iter:
                n = int(match_iter.group(1))
            match = re.search(r"Key:\s+(.*?)\s+MEAN:\s+([0-9.eE+-]+)\s+VARIANCE:\s+([0-9.eE+-]+)", line)
            if match:
                key1, key2 = match.group(1).split(' ')
                key = (key1, key2)
                mean = float(match.group(2))
                var = float(match.group(3))
                calculate_confidence_interval(key1, key2, change_values(mean), var, n, conf_interval)
                rsa_dict[key] = mean
        mat = create_matrix(rsa_dict)
        plot_rsa_score(mat, config)
        return conf_interval


def plot_confidence_intervals(conf_int, config):
    pairs = list(conf_int.keys())
    means = [conf_int[p][0] for p in pairs]
    lowers = [conf_int[p][1] for p in pairs]
    uppers = [conf_int[p][2] for p in pairs]
    yerr = [np.array(means) - np.array(lowers), np.array(uppers) - np.array(means)]
    x_labels = [f"{f}-{s}" for f, s in pairs]
    x = np.arange(len(pairs))

    plt.figure(figsize=(10, 6))
    plt.errorbar(x, means, yerr=yerr, fmt='o', capsize=5, linestyle='None', color='crimson')
    plt.xticks(x, x_labels, rotation=45, ha='right')
    plt.ylim(min(lowers)-0.05, 1)
    plt.ylabel("Confidence Interval")
    plt.title(f"Confidence Intervals for RSA similarities using {config.get_method()}")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    plt.savefig(config.filename("plots/confidence_interval/confidence_interval"))
    plt.close()


def plot_results_from_file(filename, config):
    if not os.path.isfile(filename):
        raise FileNotFoundError(filename)
    root = os.path.dirname(filename)
    print(f"Processing directory: {root}")

    confidence_interval = run_confint_plotting(filename, config)
    plot_confidence_intervals(confidence_interval, config)

