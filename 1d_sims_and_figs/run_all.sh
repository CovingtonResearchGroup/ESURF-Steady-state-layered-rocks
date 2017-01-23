#!/bin/sh
#This script will execute all python scripts in an order that will
#generate simulation outputs and create Figures 3-9 from the manuscript

#Note: This will take a while (approx. 30 minutes, depending on machine)

#Runs simulations and generates animations
python high_uplift_sims.py
python low_uplift_sims.py
python knickpoint_damping.py
#Creates figures
python stream_power_figs.py #Figs 3-5
python contrast-with-baselevel-equilibrium.py #Fig 6
python thickness_figures.py #Fig 7
python lambda.py #Fig 8
python knickpoint_damping_figs.py #Fig 9
