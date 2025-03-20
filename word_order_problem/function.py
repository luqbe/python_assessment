
def word_order(n,word):
    word_occ = {}
    for _ in range(n):
        word = str(input())

        if word not in word_occ:
            word_occ[word] = 1
        else:
            word_occ[word] += 1
    distinct_words = list(word_occ.keys())
    occurrences = list(word_occ.values())

    return len(distinct_words), occurrences

