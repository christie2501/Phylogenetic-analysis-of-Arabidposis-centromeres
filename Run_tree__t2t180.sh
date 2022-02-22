source activate $HOME/miniconda3/
export PATH=$HOME'/miniconda3/bin/':$PATH

pathhome='/home/cpkp2/001Fasta/all_accessions_vlyrata'
myaccession=t2t_rootly.Fasta
outputdir1='/production/cpkp2/000test/mafftoutput'
mkdir -p $outputdir1 #make output directory
cd $outputdir1 #cd into output directory so that output files are deposited there

outgroup=MN47Hifi_Chr7_21640788,MN47Hifi_Chr7_21502736,MN47Hifi_Chr7_19801112,MN47Hifi_Chr7_19442642,MN47Hifi_Chr4_9878196,MN47Hifi_Chr4_8268257,MN47Hifi_Chr4_8005271,MN47Hifi_Chr4_9758624,MN47Hifi_Chr1_20431762,MN47Hifi_Chr1_19332123,MN47Hifi_Chr1_20776504,MN47Hifi_Chr3_16818902,MN47Hifi_Chr3_18083739,SiberianAly_Chr3_18879862,SiberianAly_Chr3_17326644,SiberianAly_Chr3_17294063,SiberianAly_Chr3_16987581,SiberianAly_Chr3_20375047,SiberianAly_Chr4_9143917,SiberianAly_Chr4_8520280,SiberianAly_Chr4_9211445,SiberianAly_Chr4_11041890,SiberianAly_Chr7_19580665,SiberianAly_Chr7_18719480,SiberianAly_Chr1_18903696
#create list of outgroup sequences for tree to be rooted with

mafft ${pathhome}/${myaccession} > ${myaccession}_mafft.Fasta #mafft with default settings

iqtree -s ${myaccession}_mafft.Fasta -o ${outgroup} -pre ${myaccession} -m TIM2+I+G -bb 1000 -T 16
#iqtree using mafft output file, root tree with 'outgroup' variable, call the file based off accession's name,
# do bootstrapping with 1000 replicates, thread 16 times
