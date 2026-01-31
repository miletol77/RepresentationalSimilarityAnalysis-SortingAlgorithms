# Representational Similarity Analysis on Sorting Algorithms

This project has been developed to investigate the performance of Representational Similarity Analysis (RSA) on sorting algorithms as stated in the paper "Can RSA understand Sorting Algorithms?". The precise description of how everything works can be found in the paper.

Below a brief explaination of how to use the code.

In order to execute this the only sotware and libraries needed are python 3.7, scipy 1.7.3 and numpy 1.21.5.

On execution the user can set command line arguemnts to set specific simulation parameters i.e. numer of iterations, size of one array, which distance metric should be used, wheter each step RDM and the result of each independent run shouold be plotted, which method for mapping intermediate states of two different sorting algorithms should be used (DTW or LSA) and if a full simulation should be done i.e default to 32 iterations on arrays fo size 50 for DTW and LSA each using Spearman's Rank and 32 iterations on arrays fo size 50 for DTW and LSA each using Kendall Tau distance.
Setting the parameter for a full simulation does not require setting other parameters. If other parameters (except array size and number of iterations) are set, they are ignored.

The results are automatically logged and the plots are automatically saved using unique names that reveral what the plot represents.
In the directory plots there are 4 sub-directories:
confidence_interval -> contains the plot of the confidence inverval after one simulation is complete
result_simulation -> Contains the resulting RSA matrix after one simulation
rsa-score (only plotted if command line parameter set) -> contains plots of the RSA matrix after each single iteration
RDMs (only plotted if command line parameter set) -> Contains the Representational Dissimilarity matrices that are used to find map the intermediate states of two algorithms

The simulation is performed using all available hardware threads, however if this is not wished, it can be turned off by specifying the number of threads to use in the file iteration.py on line 60
