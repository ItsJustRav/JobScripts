#!/bin/bash

## Commands have been commented out with "##". Un-comment as needed.
## Alternatively, copy the needed to main run script.

## echo ##################################
# Set up submit to ...
#SBATCH --job-name="JobName"           ## Job name
#SBATCH --time=12:00:00                ## Time limit hrs:mm:ss
#SBATCH --nodes=2                      ## Number of nodes
#SBATCH --ntasks-per-node=24           ## Number of tasks per per node
#SBATCH --error=err_%job-name.log      ## Error log
#SBATCH --output=out_%job-name.log     ## Output log
#SBATCH --mail-user=email@uni.ac.uk    ## E-mail for notifications
#SBATCH --mail-type=<ALL>              ## Types of notification for e-mails
#SBATCH --partition=que                ## Job que to submit
## echo ##################################

nodes=$SLURM_JOB_NUM_NODES            ## Number of nodes
cores=$SLURM_CPUS_ON_NODE             ## Number of cores

# Load Modules and setup
## Commented out due to these being included in .bashrc file for load at login.
## module load openmpi/intel-opa/gcc-hfi/64/1.10.4