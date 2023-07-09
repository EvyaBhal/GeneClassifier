# GeneClassifier
A gene calssification app using IMM implementation in python



# How to run
Run on Darwin server - get access to TH Darwin server
need to run from path of the FASTA files ( or edit src code to receive path to files locally)
data files are located in /home/IMM-data (softlink)

# Action Items
1. Missing module to parse FASTA files - @Arbel
2. GeneClassiffier.py to use IMMs and train all of them to get the max probability of a sequence classified to label X - @Evyatar Bhalker
3. Missing implementation for weight initial values calculation - should be inside each IMM since each model is responsible for it's own genome - @Evyatar
4. specific data types and converting from/to string - depends on FASTA parser implementation using Bio lib.
5. verify files are accessible to all relevant users - @Evyatar
