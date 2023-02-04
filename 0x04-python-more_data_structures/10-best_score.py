#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best = ""
    k = list(a_dictionary)
    for i in range(len(a_dictionary)):
        value = a_dictionary[k[i]]
        key = k[i]
        if (i + 1) < len(a_dictionary) and a_dictionary[k[i + 1]] > value:
            best = k[i + 1]
    return best
