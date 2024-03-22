This Python is custom made no additional library is been used. Although this work can be done using Python regex using Findall function.

import re
dna="AGGGTAAGGA"
pattern="GGG"

count=re.findall(pattern, dna_sequence)
matches=len(count)
