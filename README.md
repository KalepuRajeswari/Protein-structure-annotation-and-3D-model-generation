# Protein Sequence Annotation & Structure Generation Methods - Scripts

This repository contains scripts developed for the protein sequencen and its structure annotation method. These scripts are divided into modules, each responsible for specific tasks in the pipeline.

---

## System Requirements

- **Python**: Version 3 or higher
- **Biopython**: A Python library for biological computation. To install, run:

  To install the `biopython` module in Linux, run the following command in the terminal:
  ```bash
  python3 -m pip install biopython
  ```
  To install the `biopython` module in windows, use following command in cmd:
  ```bash
  py -3 -m pip install biopython
  ```
  
## Module 2: Sequence Preprocessing
1. combine_fasta_files.py

    This script combines individual multi-FASTA files into a single multi-FASTA file..

2. redundancy_seq_removal.py

    This script removes redundant sequences from a multi-FASTA file.

3. partial_seq_removal.py

    This script removes partial or incomplete sequences from a multi-FASTA file.

## Module 4: Protein Structure Prediction and Analysis
1. multi_to_single_fasta.py

    This script separates a multi-FASTA file into individual protein FASTA files for ColabFold, as ColabFold requires individual protein sequences to generate structures.

2. process_json_to_csv.py

    This script extracts relevant metrics (pLDDT, pTM, Max PAE) from ColabFold output and converts them into a CSV format for downstream analysis.

## How to Run the Scripts

To execute a script, use the following command in the terminal:

```bash
python3 <script_name>.py
```

### Example
  ```bash
  python3 combine_fasta_files.py
   ```

This will run the specified script and perform its designated task.


if you are using any of the scripts, or workflow, please cite


Rajeswari K, Azzmer A.A.H, Maizom H, Norfarhan M. A., Nor Azlan N.M. (2025), A Computational Pipeline for Functional Annotation and Structural Characterization of Insect Gustatory Proteins. 

