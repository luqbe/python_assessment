from math import comb


def probability_of_a(n, letters, k):

    count_a = letters.count('a')

    if count_a == 0:
        return 0.0

    total_ways = comb(n, k)  # k element from n
    non_a_ways = comb(n - count_a, k) if k <= (n - count_a) else 0  # Ways to pick k without 'a'

    probability = 1 - (non_a_ways / total_ways)
    return round(probability, 4)  # Round to 4 decimal places



