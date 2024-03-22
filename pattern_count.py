#Bioinformatics 1: Pattern Count in the DNA sequence
"""
This Code will be use to count the pattern in the DNA sequence this can help to
find the Ori region in the sequnce and DnaA binding site (or Dna Box).....
We Will call an input Function that take DNA sequence as an String and
add .upper() function to covert the DNA sequence in uper case
"""
dna_sequence=str(input("Enter your DNA Sequence: ")).upper()


"""
We Will call an input Function that take DNA sequence as an String and
add .upper() function to covert the DNA sequence in uper case
"""
pattern=str(input("Enter your Pattern: ")).upper()

#we will also required to cheack the length of the Pattern and store in the vaarible called pattern_length

pattern_length=len(pattern)

"""
we will use len() to count the nucleotides in provided DNA sequence and
will store it in the varible called "dna_length"
"""
dna_length=len(dna_sequence)

"""
we will use the k.mer method to count particular pattern in the dna_sequence provided
first to do this we will create a pattern_count funtion
"""
def pattern_count(pattern,dna_sequence):
#we took count as a variable to store the value of pattern counted
  count=0
#Used For i in range that ranges total dna to pattern length+1 (cause indexing starts with 0)
  for i in range(dna_length-pattern_length+1):
#conditional statement states count the pattern with slided window (i:i+ pattern_length) of the pattern and if matches add 1 or if not add 0)
    if dna_sequence[i:i+ pattern_length]==pattern:
      count += 1
    else:
      count += 0
#stored the function in the count to print or you can simply return count

count= pattern_count(pattern,dna_sequence)

#converted the count in the string to concatinate the integer value with string
print("Total count of Pattern: " + pattern + "in DNA sequence is : " + str(count) )
