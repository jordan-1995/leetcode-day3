from collections import Counter

def checkInclusion(s1, s2):
    s1_length = len(s1)
    s2_length = len(s2)

    if s1_length > s2_length:
        return False

    s1_hash = Counter(s1)

    for i in range(s2_length):
        if Counter(s2[i:s1_length + i]) == s1_hash:
            print("Substring exist")

    return False

checkInclusion("akshay", "arun more")