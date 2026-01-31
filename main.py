import argparse

from iteration import run_simulation
from run_config import RunConfig


def parse_args():
    parser = argparse.ArgumentParser(description="Run simulation with configurable parameters.")

    parser.add_argument(
        "--size_array",
        type=int,
        default=50,
        help="Size of each array (non-negative integer)."
    )

    parser.add_argument(
        "--num_iterations",
        type=int,
        default=32,
        help="Number of iterations (non-negative integer)."
    )

    parser.add_argument(
        "--distinct_arrays",
        action="store_true",
        help="Use distinct arrays."
    )

    parser.add_argument(
        "--dynamic_time_warping",
        action="store_true",
        help="Enable dynamic time warping."
    )

    parser.add_argument(
        "--kendall_tau",
        action="store_true",
        help="Use Kendall tau instead of Spearman."
    )

    parser.add_argument(
        "--full_simulation",
        action="store_true",
        help="Whether to run full simulation."
    )

    parser.add_argument(
        "--plot_rdm",
        action="store_true",
        help="if plotting every RDM is required."
    )

    parser.add_argument(
        "--plot_rsa_matrix",
        action="store_true",
        help="if plotting every rsa_matrix is required."
    )

    return parser.parse_args()


def full_simulation_configs(base_args):
    for kendall in [False, True]:
        for dtw in [False, True]:
            yield RunConfig(
                size_array=base_args.size_array,
                num_iterations=base_args.num_iterations,
                distinct_arrays=False,
                dynamic_time_warping=dtw,
                kendall_tau=kendall,
                plot_rdm=args.plot_rdm,
                plot_rsa_matrix = args.plot_rsa_matrix,
            )


if __name__ == '__main__':
    args = parse_args()
    size_array = args.size_array
    num_iterations = args.num_iterations
    distinct_arrays = args.distinct_arrays
    dynamic_time_warping = args.dynamic_time_warping
    kt = args.kendall_tau
    plot_rdm = args.plot_rdm
    plot_rsa_matrix = args.plot_rsa_matrix

    if args.full_simulation:
        for config in full_simulation_configs(args):
            print(f"Running {config.tag()}")
            run_simulation(config)
    else:
        config = RunConfig(
            size_array=args.size_array,
            num_iterations=args.num_iterations,
            distinct_arrays=args.distinct_arrays,
            dynamic_time_warping=args.dynamic_time_warping,
            kendall_tau=args.kendall_tau,
            plot_rdm=args.plot_rdm,
            plot_rsa_matrix = args.plot_rsa_matrix,
        )
        print(f"Running {config.tag()}")
        run_simulation(config)

