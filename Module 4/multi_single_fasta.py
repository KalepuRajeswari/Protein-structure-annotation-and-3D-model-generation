# Python script to separate a multi-FASTA file into single-FASTA files with the protein ID as a file name.
# Start of the script

from Bio import SeqIO
import os

# input and output files, give the path according to your data
input_file = "/home/INBIOSIS/Documents/colab/Rpw-prot-seq.fasta"
output_dir = "/home/INBIOSIS/Documents/colab/single_files_dir"

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Parse the multi-FASTA file and save each sequence to a separate file
count =0
for record in SeqIO.parse(input_file, "fasta"):
    output_file = os.path.join(output_dir, f"{record.id}.fasta")
    with open(output_file, "w") as f:
        SeqIO.write(record, f, "fasta")
        print(output_file, + count)
        count = count + 1;
print(f"Total sequences processed: {count}")

# End of the script
