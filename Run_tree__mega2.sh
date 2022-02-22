source activate $HOME/miniconda3/
export PATH=$HOME'/miniconda3/bin/':$PATH

pathhome='/home/cpkp2/001Fasta/all_accessions_vlyrata'
myaccession=megatree_2a.Fasta
outputdir1='/production/cpkp2/000test/mafftoutput'
mkdir -p $outputdir1 #make output directory
cd $outputdir1 #cd into output directory so that output files are deposited there

mafft ${pathhome}/${myaccession} > ${myaccession}_mafft.Fasta #mafft with default settings

iqtree -s ${myaccession}_mafft.Fasta -o capsella160,capsella175 -pre ${myaccession} -m TIM2+I+G -bb 1000 -T 16
#iqtree using mafft output file, root tree with outgroup of capsella sequences, call the file based off accession's name,
# do bootstrapping with 1000 replicates, thread 16 times

