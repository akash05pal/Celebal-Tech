def capitalize(s):
    return ' '.join(word.capitalize() for word in s.split(' '))

if __name__ == "__main__":
    s = input()
    print(capitalize(s)) 