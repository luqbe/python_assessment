from iterators_problem.function import *
n = int(input("Enter n: "))  # Number of elements in list
letters = input("Enter space-separated letters: ").split()  # List of letters
k = int(input("Enter k: "))  # Number of indices

print("Probability:", probability_of_a(n, letters, k))