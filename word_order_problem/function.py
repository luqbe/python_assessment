
def word_order(n,word):
    word_occ = {}
    for words in word:
        if words not in word_occ:
            word_occ[words] = 1
        else:
            word_occ[words] += 1
    distinct_words = list(word_occ.keys())
    occurrences = list(word_occ.values())

    return len(distinct_words), occurrences

