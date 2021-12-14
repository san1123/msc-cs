from collections import Counter

no_of_seq=int(input("Enter how many sequences is to be entered:"))
sequence=[]
lst2=[]
consensus=[]


def take_input(sequence):
    global no_of_element
    seq=input("Enter the seq in comma separated format:")
    element=seq.split(",")
    if not sequence:
        no_of_element=len(element)
    if len(element)==no_of_element:
        sequence.append(element)
        return True
    else:
        return False

for i in range(no_of_seq):
    check=take_input(sequence)
    if not check:
        print("Please enter the seq of correct length")
        check=take_iput(sequence)
        if not check:
            break

#creates a dynamic empty list to store value columnwise
for i in range(len(sequence[0])):
    lst2.append([])


#Creates list columnwise
for i in range(len(sequence[0])):   #length of first element of whole sequence
    for j in range(len(sequence)):  #no_of_ssequences
        lst2[i].append(sequence[j][i])

#counting the occurence of elements and appending as per need
for j in lst2:
    nul_list=[]
    j=[x for x in j if x != '-']
    counter=Counter(j)
    if len(list(counter.keys()))==1:
        consensus.append(list(counter.keys())[0].upper())
    elif len(list(counter.keys()))>1:
        max_value=max(counter.values())
        for i in range(len(list(counter.keys()))):
            if max_value==counter.get(list(counter.keys())[i]):
                nul_list.append(list(counter.keys())[i].upper())
        if len(nul_list)>1:
            consensus.append(nul_list)
        else:
            consensus.append(nul_list[0].lower())

#joining with /
for i in range(len(consensus)):
    final_str=''
    if type(consensus[i])==list:
        final_str='/'.join(consensus[i])
        consensus[i]=final_str
print("Consensus: ",consensus)
