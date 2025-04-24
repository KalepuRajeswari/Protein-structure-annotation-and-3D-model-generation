# Script to combine all downloaded individual fasta files into one multi-FASTA file
# Start of the Script

from Bio import SeqIO
import os
def combine_fasta_files(input_files, output_file):
    with open(output_file, 'w') as outfile:
        for file in input_files:
            for record in SeqIO.parse(file, "fasta"):
                SeqIO.write(record, outfile, "fasta")
    print(f"Combined FASTA file created at: {output_file}")

# Specify the input and output directory names
input_directory = "C:/Users/INBIOSIS/Desktop/Combine-fasta"
output_file = "C:/Users/INBIOSIS/Desktop/Combine-fasta/Rpw-prot-seq.fasta"

# Gather all FASTA files from the directory
fasta_files = [os.path.join(input_directory, f) for f in os.listdir(input_directory) if f.endswith(".fasta")]

# Combine the FASTA files
combine_fasta_files(fasta_files, output_file)

# End of the Script
