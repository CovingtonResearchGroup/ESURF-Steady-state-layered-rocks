These are the FastScape.in input files for the FastScape simulations run for Figure 10 and the scripts used to generate the figure. Outputs from FastScape were read into Landlab v0.2 using DEMImport_v2.py. This script calculates flow routing and chi and generates stream profiles. Landlab v0.2 did not have a function to calculate chi, so we created a function to do so in DEMImport_v2.py. However, the current version of Landlab (v1.0.2) already contains a built-in function to calculate chi, so this step is no longer necessary. DEMImport_v2.py creates pickle files of outputs. The names of these pickle files and the image files of the DEMs for different FastScape simulations need to be edited appropriately in prf_subplot.py to create Figure 10.  

The FastScape input files are:

FastScape_0.66.in - n=2/3 case

FastScape_1.in - n=1 case

FastScape_1.5.in - n=3/2 case
