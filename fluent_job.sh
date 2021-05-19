#!/bin/bash

## Commands have been commented out with "##". Un-comment as needed.
## Alternatively, copy the needed to main run script.

####################################
# Set up submit to ...
#SBATCH --job-name="JobName"           ## Job name
#SBATCH --time=12:00:00                ## Time limit hrs:mm:ss
#SBATCH --nodes=2                      ## Number of nodes
#SBATCH --ntasks-per-node=24           ## Number of tasks per per node
#SBATCH --error=err_%job-name.log      ## Error log
#SBATCH --output=out_%job-name.log     ## Output log
#SBATCH --mail-user=email@northumbria.ac.uk    ## E-mail for notifications
#SBATCH --mail-type=ALL                ## Types of notification for e-mails
#SBATCH --partition=24hour             ## Job que to submit <24hour, 48hou, 120hour>
####################################

nodes=$SLURM_JOB_NUM_NODES            ## Number of nodes
cores=$SLURM_CPUS_ON_NODE             ## Number of cores

# Load Modules and setup
## Commented out due to these being included in .bashrc file for load at login.
## module purge  ## Remove all modules
module add openmpi/intel-opa/gcc-hfi/64/1.10.4  ## Load dedicated MPI module
module add gcc/5.2.0 ## Load GCC module
# module add slurm/15.08.6 ## Load the SLURM module
module load ANSYS/2021R1  ## Load the ANSYS module

# Case Details
# fluent.journal  ## Journal file name
JOURNALFILE= ab_iso_kwsst/run_case.journal

# Execute Solver
fluent 3d -g -slurm -t$NPROCS -mpi=openmpi -i $JOURNALFILE > fluent.log


