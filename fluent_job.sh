#!/bin/bash

# Commands have been commented out with "##". Un-comment as needed.
# Alternatively, copy the needed to main run script.

# ###################################
# Set up submit to ...
# Job name
#SBATCH --job-name="JobName"  

# Time limit hrs:mm:ss         
#SBATCH --time=12:00:00

# Number of nodes                
#SBATCH --nodes=2           

# Number of tasks per per node
#SBATCH --ntasks-per-node=24 

# Que/Partition for submission
#SBATCH --partition=24hour             

# Error log
#SBATCH --error=err_%job-name.log

# Output log
#SBATCH --output=out_%job-name.log

# E-mail for notifications
#SBATCH --mail-user=r.t.b.ranaweera@northumbria.ac.uk

# Types of notification for e-mails
#SBATCH --mail-type=<ALL>

# Job que to submit
#SBATCH --partition=que                
# ###################################

# Get number of nodes
nodes=$SLURM_JOB_NUM_NODES
# Get number of cores            
cores=$SLURM_CPUS_ON_NODE             

# Load Modules and setup
# Commented out due to these being included in .bashrc file for load at login.
# module purge  ## Remove all modules
module add openmpi/intel-opa/gcc-hfi/64/1.10.4  ## Load dedicated MPI module
# Load GCC module
# module add gcc/5.2.0
# Load the SLURM module
module add slurm/15.08.6
# Load the ANSYS module
module add ANSYS/18.0

# Case Details
# JOURNALFILE= ## fluent.journal  ## Journal file name
FLUENT = ## /ansys_inc/v190/fluent/bin/fluent ## Module path

# Execute Solver
$FLUENT 3d -g -slurm -t$NPROCS -mpi=openmpi -i $JOURNALFILE > fluent.log


