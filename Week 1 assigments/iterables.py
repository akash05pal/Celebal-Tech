from itertools import combinations

n = int(input())
arr = input().split()
k = int(input())

count = 0
for combo in combinations(arr, k):
    if 'a' in combo:
        count += 1

print(count / len(list(combinations(arr, k))))
