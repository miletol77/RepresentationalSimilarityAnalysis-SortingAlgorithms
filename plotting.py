import os
import matplotlib.pyplot as plt
from numpy import arange, ndenumerate

from run_config import RunConfig


def show_matrix(ax, matrix, alg_names):
    im1 = ax.matshow(matrix)
    #ax.set_title(title, fontsize=15)
    ax.set_xticks(arange(matrix.shape[0]))
    ax.set_xticklabels(alg_names, rotation=-45, ha='right', fontsize=14)
    ax.set_yticks(arange(matrix.shape[0]))
    ax.set_yticklabels(alg_names, rotation=45, ha='right', fontsize=14)
    for (i, j), z in ndenumerate(matrix):
        ax.text(j, i, '{:0.2f}'.format(z), ha='center', va='center', fontsize=14)
    return im1


def plot_rsa_score(rsa_score, alg_names, config: RunConfig):
    fig, axes = plt.subplots(figsize=(11, 11))
    im = show_matrix(axes, rsa_score, alg_names)
    fig.colorbar(im, orientation='vertical')
    fig.suptitle("RSA Score of Sorting Algorithms", fontsize=25)

    plt.savefig(config.filename("plots/rsa-score/rsa_score"))
    plt.close(fig)


def show_rdm(ax, matrix, key):
    ax.matshow(matrix, aspect='auto')
    ax.set_box_aspect(1)
    ax.set_title(f"RDM of {key}", fontsize=20)
    ax.set_xlabel("Intermediate-States", fontsize=15)
    ax.set_ylabel("Intermediate-States", fontsize=15)


def plot_cost_mat(ax, mat, rows, cols, dtw, key1, key2):
    ax.matshow(mat, aspect='auto')
    ax.set_box_aspect(1)
    if dtw:
        ax.plot(cols, rows, color='red', marker='none', alpha=1)
    else:
        ax.scatter(cols, rows, color='red', marker='x', alpha=0.7)
    ax.set_title(f"Cost Matrix", fontsize=20)
    ax.set_xlabel(f"Intermediate-States {key2}", fontsize=13)
    ax.set_ylabel(f"Intermediate-States {key1}", fontsize=13)


def plot_rdm_arrays_chosen(key1, key2, rdm1, rdm2, cost_mat, row_col, axes, dtw):
    show_rdm(axes[0], rdm1, key1)
    show_rdm(axes[1], rdm2, key2)
    plot_cost_mat(axes[2], cost_mat, row_col[0], row_col[1], dtw, key1, key2)


def plot_cost_rows_rdm(all_rdms, cost_mat, row_col, config: RunConfig):
    rows = len(all_rdms.keys())
    fig, axes = plt.subplots(rows, 3, figsize=(25, 150), gridspec_kw={'wspace': 0.5, 'hspace': 0.5})
    idx = 0
    for key, value in all_rdms.items():
        ax = axes[idx]
        key1, key2 = key
        plot_rdm_arrays_chosen(key1, key2, value[0], value[1], cost_mat[key], row_col[key], ax, config.dynamic_time_warping)
        idx += 1
    fig.suptitle("RDM's of compared Algorithms along Cost Matrix with indexes chosen", fontsize=45)
    fig.subplots_adjust(top=0.95)

    plt.savefig(config.filename("plots/RDMs/rdm-wt-indexes-chosen"))
    plt.close(fig)

