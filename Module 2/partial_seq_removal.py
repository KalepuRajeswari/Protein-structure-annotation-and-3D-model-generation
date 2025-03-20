
# Program to remove the partial protein sequences in multi fasta file
# Start of the program

from Bio import SeqIO

def remove_partial_sequences(input_fasta, output_fasta):
    with open(output_fasta, "w") as out_fh:
        for record in SeqIO.parse(input_fasta, "fasta"):
            if "partial" not in record.description:
                SeqIO.write(record, out_fh, "fasta")

input_fasta = "C:/Users/INBIOSIS/Desktop/RPW-fasta/Redundancy_removed_sequences.fasta"  # Replace with your actual input file
output_fasta = "C:/Users/INBIOSIS/Desktop/RPW-fasta/Partial_sequences_removed.fasta"  # Replace with your desired output file
remove_partial_sequences(input_fasta, output_fasta)

#End of the program
