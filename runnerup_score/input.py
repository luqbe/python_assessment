from runnerup_score.function import*

n = int(input("Enter the number of scores: "))
scores = list(map(int, input("Enter the scores separated by space: ").split()))
print(runner_up(scores))