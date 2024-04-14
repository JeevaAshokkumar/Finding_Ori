def MinimumSkew(Genome):
    positions = [] # output variable
    skew_array = SkewArray(Genome)
    values = min(skew_array)
    for i in range(len(Genome)):
        if skew_array[i] == values:
            positions.append(i)
    return positions
def SkewArray(Genome):
    skew_array =[0]
    for i in range(1,len(Genome)+1):
        if Genome[i-1] == "C":
            skew_array.append(skew_array[i-1] - 1)
        elif Genome[i-1] == "G":
            skew_array.append(skew_array[i - 1] + 1)
        else:
            skew_array.append(skew_array[i - 1])
    return skew_array
def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(symbol, ExtendedGenome[i:i+(n//2)])
    return array
# Input:  Strings Genome and symbol
# Output: FasterSymbolArray(Genome, symbol)
def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    # look at the first half of Genome to compute first array value
    array[0] = PatternCount(symbol, Genome[0:n//2])
    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        array[i] = array[i-1]
        # the current array value can differ from the previous array value by at most 1
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array
# Input:  Strings Text and Pattern
# Output: The number of times Pattern appears in Text
# HINT:   This code should be identical to when you last implemented PatternCount
def PatternCount(Pattern, Text):
    count = 0 # output variable
    for i in range(len(Text)):
        if Text[i:i+len(Pattern)]==Pattern:
            count+=1
    return count
# Input:  A string Text and an integer k
# Output: A list containing all most frequent k-mers in Text
def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key]==m:
            words.append(key)
    return words
def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] = 0
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        freq[Pattern] += 1
    return freq
# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):   
    Pattern = Reverse(Pattern)
    Pattern = Complement(Pattern)
    return Pattern
def Reverse(Pattern):
    rev=''
    for char in Pattern:
        rev=char+rev
    return rev
def Complement(Pattern):
    comp = ""
    for char in Pattern:
        if char == "A":
            char = char.replace("A","T")
        elif char == "C":
            char = char.replace("C","G")
        elif char == "G":
            char = char.replace("G","C")
        elif char == "T":
            char = char.replace("T","A")
        comp = comp + char
    return comp
def PatternMatching(Pattern, Genome):
    positions = [] # output variable
    for i in range(len(Genome)-len(Pattern)+1):
        if Genome[i:i+len(Pattern)]==Pattern:
            positions.append(i)
    return positions
