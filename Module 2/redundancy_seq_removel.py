# Script to remove the redundant protein sequences in a multi-FASTA file
# Start of the Script

from Bio import SeqIO

# input and output files, give path according to your data
input_file = "/home/inbiosis/Documents/Rpw-prot-seq.fasta"
output_file = "/home/inbiosis/Documents/Rpw-prot-seq-Redundant-removal.fasta"

# dictionary to store unique sequences
sequences = {}
# Iterate over input FASTA file and store unique sequences in the dictionary
for record in SeqIO.parse(input_file, "fasta"):
    sequence = str(record.seq)
    if sequence not in sequences.values():
        sequences[record.id + " " + record.description] = sequence

# Write unique sequences to output file
with open(output_file, "w") as outfile:
    for seq_id, sequence in sequences.items():
        if seq_id.__contains__(" "):
            words = seq_id.split()
            seq_id = " ".join(words[1:])
        outfile.write(">" + seq_id + "\n" + sequence + "\n\n")

# End of the Script
