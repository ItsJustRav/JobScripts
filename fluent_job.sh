#!/bin/bash

# Job Submission Script
# Job Submission Script for running ANYS Fluent CFD Case on an HPC Cluster running Linux and SLURM Workload Manager by Ravindu Ranaweera (https://github.com/ItsJustRav)
# Commands have been commented out with "##". Un-comment as needed.

# ################################################################################################
# Job Information
#SBATCH --job-name="URKE0.5"           	           ## Job name
#SBATCH --time=119:30:00                		               ## Time limit hrs:mm:ss
#SBATCH --nodes=4                      	     	           ## Number of nodes
#SBATCH --ntasks-per-node=56          	     	           ## Number of tasks per per node
#SBATCH --error=error_log_%j.log      	                 ## Error log
#SBATCH --output=sbatch_output.log                       ## Output log
#SBATCH --mail-user=r.t.b.ranaweera@northumbria.ac.uk    ## E-mail for notifications
#SBATCH --mail-type=ALL                		               ## Types of notification for e-mails
#SBATCH --partition=120hour             		               ## Job que to submit <24hour, 48hour, 120hour>
# ################################################################################################

nodes=$SLURM_JOB_NUM_NODES            ## Number of nodes
cores=$SLURM_CPUS_ON_NODE             ## Number of cores

# Number of Nodes and Cores
echo "Nodes and Cores"
echo $nodes
echo $cores
# Write out a node list to a file
scontrol show hostname $SLURM_NODELIST | tr " " "\n" > ./node_file

# Load Modules and setup
# Commented out due to these being included in .bashrc file for load at login.
# module purge  ## Remove all modules
module add openmpi/intel-opa/intel-hfi/64/1.10.4 #module add openmpi/intel-opa/gcc-hfi/64/1.10.4  ## Load dedicated MPI module
module add gcc/5.2.0 ## Load GCC module
# module add slurm/15.08.6 ## Load the SLURM module
module load ANSYS/2021R1  ## Load the ANSYS module

# Information
echo "<------------------Start------------------>"
date
echo "<--Directory Space-->"
pwd
du -sh
echo ""

# Execute Solver (replace run_case.jou with the journal file name)
# /usr/bin/time -v >> Information such as time, cpu usage, memory usage, etc.
# fluent >> execute fluent
# 3d >> 3d case (2d for 2d case, 2ddp for 2d double precission and 3ddp for 3d double precision)
# -gu >> Run with graphics minimised
# -slurm >> Workload manager
# -t<x> >> number of processors to be used
# -mpi=<mpi_type> >> MPI implementation to use use "=intel" for Oswald HPC
# -driver null >> running with no GUI to avoid errors caused by plot / figure export
# -pib.infinipath >> To use the the high performance Omnipath networking
# -cnf=$PWD/node_file  >> Creates a node list which is used to allocate tasks across multiple nodes (can add -ssh but is set by default)
# -i <journal_file_name.jou> >> Read and execute as per journal file
# -cflush >> Free the file cache buffer

echo "<--Executing Fluent-->"
/usr/bin/time -v fluent 3ddp -gu -slurm -t$((nodes*cores)) -mpi=intel -pib.infinipath -cnf=$PWD/node_file -driver null -i run_case_ustdy.jou -cflush> fluent.log
#echo "<--Fluent Finished-->"
#date
#echo  ""

# Encode Animations 
#echo "<--Executing encode.sh-->"
#date
#chmod +x encode.sh # Make the script executable
#/usr/bin/time -v ./encode.sh>encode.log
#echo "<--encode.sh Finished-->"
#date
#echo ""

# File Operations (Organises files and folders)
#echo "<--Executing fileops.sh-->"
#date
#chmod +x fileops.sh # Make the script executable
#/usr/bin/time -v./fileops.sh>filesops.log
#echo "<--fileops.sh Finished-->"
#date
#echo ""

# Folder Size
#echo "<--Directory Space-->"
#pwd
#du -sh

# End Time Stamp
#echo "<--------------------End-------------------->"
#date
#exit
