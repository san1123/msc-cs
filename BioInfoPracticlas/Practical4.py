from random import choice, randint
from string import ascii_uppercase


# Function to generate sequences of similar or dissimilar lengths
# This function will be executed for Python v3.6+
def generate_sequences() -> tuple[list[str]]:
    char_sequence = list(ascii_uppercase)
    sequence_1 = [choice(char_sequence) for i in range(randint(8, 20))]
    sequence_2 = [choice(char_sequence) for i in range(randint(8, 20))]
    
    return sequence_1, sequence_2


# This function adds gaps to the sequence.
def add_gap(sequence : list[str], random_flag : bool) -> list[str]:
    index = randint(0, len(sequence) - 1)
    
    if not random_flag:
        index = int(input(f"Enter an integer from 0 to {len(sequence) - 1} where you want to insert the gap>\t"))
    
    sequence.insert(index, "-")
    
    return sequence


# Function to add multiple gaps in a sequence
def add_gaps(sequence_1 : list[str], sequence_2 : list[str],  random_flag : bool) -> tuple[list[str]]:
    while(len(sequence_1) != len(sequence_2)):
        if len(sequence_1) > len(sequence_2):
            sequence_2 = add_gap(sequence_2, random_flag)
        else:
            sequence_1 = add_gap(sequence_1, random_flag)
    
    return sequence_1, sequence_2


# Get the similar proteins from the user
def get_similar_proteins() -> list[list[str]]:
    number_of_similar_protein_sets = int(input("Enter the number of sets housing similar proteins>\t"))
    similar_protein_list = []
    
    print("Enter similar proteins represented as single letter representation without any delimiters.")
    
    while(number_of_similar_protein_sets > 0):
        similar_proteins = list(input("Enter similar proteins>\t"))
        similar_protein_list.append(similar_proteins)
        number_of_similar_protein_sets -= 1
    
    return similar_protein_list


# This function finds similarity between two sequences.
def find_similarity(sequence_1 : list[str], sequence_2 : list[str], similar_protein_list : list[list[str]]) -> int:
    similarity = 0
    
    for i in range(len(sequence_1)):
        for j in range(len(similar_protein_list)):
            if(sequence_1[i] == sequence_2[i]):
                continue
            
            if(sequence_1[i] in similar_protein_list[j]) and (sequence_2[i] in similar_protein_list[j]):
                similarity += 1
    
    print(f"Similarity value for Sequence 1 and Sequence 2 is:\t{similarity}")
    
    return similarity


# This functions finds identity between the two sequences
def find_identity(sequence_1 : list[str], sequence_2 : list[str]) -> int:
    identity = 0
    
    for i in range(len(sequence_1)):
        if sequence_1[i] == sequence_2[i]:
            identity += 1
    
    print(f"Identity value for Sequence 1 and Sequence 2 is:\t{identity}")
    
    return identity


# This function calculates the total number of gaps in the sequences
def count_gaps(sequence_1 : list[str], sequence_2 : list[str]) -> int:
    return sequence_1.count('-') + sequence_2.count('-')


# This function calculates percent matches for the two sequences
def get_percent_matches(sequence_1 : list[str], sequence_2 : list[str]) -> float:
    similar_protein_list = get_similar_proteins()
    
    similarity = find_similarity(sequence_1, sequence_2, similar_protein_list)
    
    identity = find_identity(sequence_1, sequence_2)
    
    return ((similarity + identity) / (len(sequence_1) - count_gaps(sequence_1, sequence_2))) * 100


if __name__ == "__main__":
    print("Percent match calculator for two sequences in Python")
    is_random_sequences = input("Do you want the sequences to be randomly generated? [Yes]/No >\t")
    
    sequence_1, sequence_2 = generate_sequences()
    if (is_random_sequences.lower() == "no"):
        print("Enter the two sequences. The two sequences should not have any delimiters.\nPlace '-' as a gap (if necessary)")
        sequence_1 = list(input("Enter sequence 1>\t"))
        sequence_2 = list(input("Enter sequence 2>\t"))
    
    print("Sequence 1 is:\t", sequence_1)
    print("Sequence 2 is:\t", sequence_2)
    
    random_gaps = input("Do you want the gaps to be randomly added? [Yes]/No >\t")
    random_flag = True
    
    if (random_gaps.lower() == "no"):
        random_flag = False
    
    sequence_1, sequence_2 = add_gaps(sequence_1, sequence_2, random_flag)
    
    print("Sequence 1 after adding gaps:\t", sequence_1)
    print("Sequence 2 after adding gaps:\t", sequence_2)
    
    print(f"Percent matches in sequence 1 and sequence_2 is: {get_percent_matches(sequence_1, sequence_2)}%")
    
    
        
