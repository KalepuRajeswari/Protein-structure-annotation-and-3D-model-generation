from Bio import SeqIO

# input and output files
input_file = "C:/Users/INBIOSIS/Desktop/RPW-fasta/combined_fasta_file.fasta"
output_file = "C:/Users/INBIOSIS/Desktop/RPW-fasta/Redundancy_removed_sequences.fasta"

# dictionary to store unique sequences
sequences = {}


# iterate over input FASTA file and store unique sequences in dictionary
for record in SeqIO.parse(input_file, "fasta"):
    sequence = str(record.seq)
    if sequence not in sequences.values():
        sequences[record.id + " " + record.description] = sequence


# write unique sequences to output file
with open(output_file, "w") as outfile:
    for seq_id, sequence in sequences.items():
        if seq_id.__contains__(" "):
            words = seq_id.split()
            seq_id = " ".join(words[1:])
        outfile.write(">" + seq_id + "\n" + sequence + "\n\n")
print(f"output file created at: {output_file}")
