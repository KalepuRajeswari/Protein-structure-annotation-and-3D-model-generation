# Script to remove the partial protein sequences in a multi-FASTA file
# Start of the Script

from Bio import SeqIO
def remove_partial_sequences(input_fasta, output_fasta):
    with open(output_fasta, "w") as out_fh:
        for record in SeqIO.parse(input_fasta, "fasta"):
            if "partial" not in record.description:
                SeqIO.write(record, out_fh, "fasta")

# input and output files, give path according to your data
input_fasta = "/home/inbiosis/Documents/Rpw-prot-seq-Redundant-removal.fasta" 
output_fasta = "/home/inbiosis/Documents/Rpw-prot-seq-partial-removed.fasta" 

#remove partial sequence function call
remove_partial_sequences(input_fasta, output_fasta)

# End of the Script
