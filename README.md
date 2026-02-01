# Representational Similarity Analysis on Sorting Algorithms

This project has been developed to investigate the performance of Representational Similarity Analysis (RSA) on sorting algorithms as stated in the paper "Can RSA understand Sorting Algorithms?". The precise description of how everything works can be found in the paper. <br>

Below a brief explaination of how to use the code. <br>

In order to execute this the only sotware and libraries needed are python 3.7, scipy 1.7.3 and numpy 1.21.5. <br>

On execution the user can set command line arguemnts to set specific simulation parameters i.e. <br>
python3 main.py <br>
*--size_array* followed by a positive interger number sets the size of the array to be sorted - defaults to 50, as described in the paper <br>
*--num_iterations* followed by a positive integer number (ideally a multiple of two), determines the number of single runs performed before the final result - defaults to 32, as described in the paper <br>
*--dynamic_time_warping* if set, it runs the simulation using Dynamic Time Warping, if not set, the simulation will use Linear Sum Assignment <br>
*--kendall_tau* if set, the distance metric to calculate the similarity between intermediate states is set to Kendall Tau Distance, else the dinstance metric is Spearman's Rank <br>
*--full_simulation* if set the simulation is run using num_iterations and size_array, using Kendall Tau with Dynamic Time Warping and Linear Sum Assignment each and Spearman's Rank with Dynamic Time Warping and Linear Sum Assignment. <br>
*--plot_rdm* if set for every iteration the Representational Dissimilarity Matrices are along with the cost matrix and the indices (LSA) and the path (DTW) along which intermediate states were chosen, is plotted. <br>
*--plot_rsa_matrix* if set for every iteration the RSA Matrix resulting from that run is plotted. These matrices are successively used to create the final result. <br>
*--distinct_arrays* can be set, setting this arguemnt varies the simulation so that each sorting algorithm receives a different algorithm to sort. RSA is then performed on the intermedaite states of the sorting algorithms emitted from the algorithms sorting different randomly generated arrays. While this was not included in the paper, as it was not focus of our work, we decided to leave it in the code. <br>

The results are automatically logged and saved in the directory **logs/** and the plots are automatically saved using unique names that reveral what the plot represents.
In the directory plots there are 4 sub-directories: <br>

**result_simulation/** -> Contains the resulting RSA matrix after one simulation <br>
**confidence_interval/** -> contains the plot of the confidence inverval after one simulation is complete <br>
**rsa-score/** (only plotted if command line parameter set) -> contains plots of the RSA matrix after each single iteration <br>
**RDMs/** (only plotted if command line parameter set) -> Contains the Representational Dissimilarity matrices that are used to find map the intermediate states of two algorithms <br>

The default simulation (num_iteration=32, size_array=50) is performed using all available hardware threads, however if this is not desired, it can be turned off by specifying the number of threads to use in the file iteration.py on line 60 <br>

If all command line arguments are omitted, the simulation will run using arrays of size 50, doing 32 iterations, using Spearman's Rank and using LSA and the plots for single RDMs and RSA Matrices will not be plotted. The final result will be plotted and saved, along with the confidence interval. <br>


