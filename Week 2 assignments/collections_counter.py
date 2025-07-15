from collections import Counter

if __name__ == '__main__':
    x = int(input())
    sizes = list(map(int, input().split()))
    n = int(input())
    earnings = 0
    inventory = Counter(sizes)
    for _ in range(n):
        size, price = map(int, input().split())
        if inventory[size]:
            earnings += price
            inventory[size] -= 1
    print(earnings) 