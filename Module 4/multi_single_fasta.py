from Bio import SeqIO
import os
# input file
#input_file = "C:/Users/INBIOSIS/Desktop/RPW-fasta/protein-multiFastaSeq.fasta"
input_file = "C:/Users/INBIOSIS/Desktop/RPW_prot/protein-multiFastaSeq.fasta"

output_dir = "C:/Users/INBIOSIS/Desktop/RPW_prot"
count =0
# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Parse the multi-fasta file and save each sequence to a separate file
for record in SeqIO.parse(input_file, "fasta"):
    output_file = os.path.join(output_dir, f"{record.id}.fasta")
    with open(output_file, "w") as f:
        SeqIO.write(record, f, "fasta")
        print(output_file, + count)
        count = count + 1;
    print(f"FASTA file created at: {output_dir}")

