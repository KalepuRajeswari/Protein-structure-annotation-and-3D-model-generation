
# Program to remove the partial protein sequences in multi fasta file
# Start of the program
from Bio import SeqIO

# input and output files, give path according to your data
fasta_file = "C:/Users/INBIOSIS/Desktop/RPW-fasta/Redundancy_removed_sequences.fasta"
output_file = "C:/Users/INBIOSIS/Desktop/RPW-fasta/Partial_sequences_removed.fasta"

# dictionary to store unique sequences
sequences = {}
# Counter for partial sequences
partial_count = 0

# Iterate over input FASTA file and store unique sequences in dictionary
for record in SeqIO.parse(fasta_file, "fasta"):
    sequence = str(record.seq)
    # Used just the record.id (no description added) for the key
    if sequence not in sequences.values():
        sequences[record.id] = sequence

# Write unique sequences to output file
with open(output_file, "w") as outfile:
    for seq_id, sequence in sequences.items():
        if "partial" in seq_id:
            partial_count += 1  # Increment the partial sequence counter
            print(f"Partial sequence found: {seq_id}")
        else:
            outfile.write(">" + seq_id + "\n" + sequence + "\n\n")
    print(f"output file created at: {output_file}")
# End of the program
