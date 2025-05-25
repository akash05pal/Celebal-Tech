from collections import OrderedDict

n = int(input())
words = OrderedDict()

for _ in range(n):
    w = input().strip()
    words[w] = words.get(w, 0) + 1

print(len(words))
print(*words.values())
