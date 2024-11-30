# CS1010S --- Programming Methodology
# Mission 5

# Note that written answers are stored in """multi-line strings"""
# to allow us to run your code easily when grading your problem set.

import csv

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows


##########
# Task 1 #
##########

def replicate(dna_strand):
    dna_base_pairings = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    
    s = ''
    for char in dna_strand:
        s = dna_base_pairings[char] + s
        
    return s

# print("## Q1 ##")
# print(replicate("AAATGC") == "GCATTT")
# print(replicate("ATTGGGCCCC") == "GGGGCCCAAT")

##########
# Task 2 #
##########

def transcribe(dna_strand):
    rna_base_pairings = {
        "A": "U",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    s = ''
    for char in dna_strand:
        s = rna_base_pairings[char] + s
    return s

def reverse_transcribe(rna_strand):
    rna_base_pairings = {
        "U": "A",
        "A": "T",
        "C": "G",
        "G": "C"
    }
    s = ''
    for char in rna_strand:
        s = rna_base_pairings[char] + s
    return s


# UNCOMMENT THE CODE BELOW AFTER YOU ARE DONE WITH TASK 2. THIS IS NOT OPTIONAL TESTING #
with open("dna.txt") as f:
    dna = f.read()
rna = transcribe(dna)

# print("## Q2 ##")
# print(rna[0:10:1]) # 'AAUAGUUUCU'
# print(transcribe("AAATGC")) # 'GCAUUU'
# print(transcribe("ATTGGGCCCC")) # 'GGGGCCCAAU'
# print(reverse_transcribe(transcribe("AAATGC"))) # 'AAATGC'
# print(reverse_transcribe("GGGGCCCAAU")) # 'ATTGGGCCCC'


##########
# Task 3 #
##########

def get_mapping(csv_filename):
    data = read_csv(csv_filename)[1:]
    
    d = {}
    for row in data:
        d[row[0]] = row[3]
        
    return d



# UNCOMMENT THE CODE BELOW AFTER YOU ARE DONE WITH TASK 3. THIS IS NOT OPTIONAL TESTING #
codon2amino = get_mapping("codon_mapping.csv")

# print("## Q3 ##")
# print(codon2amino["ACA"]) # 'T'
# print(codon2amino["AUU"]) # 'I'
# print(codon2amino["CUC"]) # 'L'
# print(codon2amino["ACU"]) # 'T'
# print(codon2amino["UAG"]) # '_'
# print(codon2amino["UGA"]) # '_'


##########
# Task 4 #
##########

def translate(rna_strand):
    codon2amino = get_mapping("codon_mapping.csv")
    
    new_strand = ''
    for i in range(len(rna_strand)):
        if rna_strand[i:i+3] == 'AUG':
            new_strand = rna_strand[i:]
            break
    
    s = ''
    if not new_strand or len(new_strand) % 3:
        return None
    stop = ['UAA', 'UAG', 'UGA']
    for i in range(0, len(new_strand), 3):
        base = new_strand[i:i+3]
        s += codon2amino[base]
        if new_strand[i:i+3] in stop:
            break
    
    if s[-1] != '_':
        return None
    return s

# print("## Q4 ##")
# print(translate("AUGUAA"))           # 'M_'
# print(translate("AGAGAUGCCCUGAGGG")) # 'MP_'
# protein = translate(rna)
# print(protein) # 'MANLTNFHLKIYIHTYIQLKHLSSGAFSLFSAHNSRSINYNYYFSFRDLNITYNHTHLTTY_'