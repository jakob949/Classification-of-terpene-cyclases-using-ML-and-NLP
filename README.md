# Classification_of_TC

The main work-process of scripts for preprocessing and performing pHMM are: <br />
sort_combined.py --> alignment_combined.py --> pHMM_DB_combined.py <br />

## Meta description of scripts 

#### sort_combined.py:
./sort_combined.py <class_vs_acc.txt> <sequence_file.txt> <br />
This program takes two files as arguments, the first file contains tab-separated classes and their corresponding accession numbers, and the second file contains all the fasta entries. The script opens the first file "class_vs_acc", reads it, and creates two dictionaries: one for small classes and one for large classes, where the accession number is the key and the class is the value. It then creates two subfolders, "small" and "large", within a folder named "class". Finally, it loops through the dictionaries, finds the corresponding sequence in the fasta file for each accession number. Then creates a new file with the class name, and adds the sequence to the file. The newly created files will be saved in the appropriate subfolder, based on the class.
alignment_combined.py:
he program is designed to use the Clustal software for MSA on files create by sort_combined.py. Then, it creates pHMM using the HMMER software for each file. 

#### pHMM_DB_combined.py <br />
This program is designed to use the HMMer function 'press' to create the finished pHMM models for both the small and large pHMMs.

#### CV_LOO.py
  ./CV_LOO.py <class_vs_acc.txt> <sequence_file.txt> <br />
  This program performs a Leave-One-Out Cross Validation pHMM analysis using the main work-process: <br />
  sort_combined.py --> alignment_combined.py --> pHMM_DB_combined.py.  <br />It takes the same inputs as sort_combined.py and iterates through the class_vs_acc file. During each iteration, it selects a single entry for testing and uses the rest for training data, which is fed into the main work-process. The program saves and outputs two files: CV_results and CV_log.
  Where the CV_results contains very basics statistics. CV_log contains all prediction values, true values, scores, and more.

#### Analysis_of_log.py
  This program contains a collection of functions to among others perform basic analysis of a CV log. It takes the log file output from CV_LOO.py and evaluates the results by producing a confusion matrix and five different performance evaluation matrices, which are illustrated in a histogram.
