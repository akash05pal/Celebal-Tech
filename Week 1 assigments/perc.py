n = int(input())
student_marks = {}

for _ in range(n):
    line = input().split()
    name, scores = line[0], list(map(float, line[1:]))
    student_marks[name] = scores

query_name = input()
avg = sum(student_marks[query_name]) / len(student_marks[query_name])
print(f"{avg:.2f}")
