def sigma_algebra(subsets_in, sample_space):
    change = True
    subsets = subsets_in.copy()
    while change:
        change = False
        subset_copy = subsets.copy()
        for s in subset_copy:
            complement = sample_space - s
            if complement not in subsets:
                subsets.add(complement)
                change = True

            for s2 in subset_copy:
                union = s | s2
                intersection = s & s2

                if union not in subsets:
                    subsets.add(union)
                    change = True

                if intersection not in subsets:
                    subsets.add(intersection)
                    change = True

    return subsets

if __name__ == "__main__":
    subsets = sigma_algebra(set((frozenset([1, 3, 5]), frozenset([4, 5, 6]))), frozenset([1, 2, 3, 4, 5, 6]))
    for s in subsets:
        print(s)
    print(len(subsets))