# Given two string, write a method to decide if one is permutation of other.

def permutation_by_sort(st1, st2):
    if len(st1) != len(st2):
        return False
    st1, st2 = sorted(st1), sorted(st2)
    for i in range(len(st1)):
        if st1[i] != st2[i]:
            return False
    return True

st1, st2 = "dog", "god"
print(permutation_by_sort(st1, st2))

    