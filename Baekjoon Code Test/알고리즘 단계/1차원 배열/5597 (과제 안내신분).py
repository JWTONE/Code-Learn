submit_student = []

for _ in range(28):
    submit_student.append(int(input()))

miss_students = []
for student in range(1, 31):
    if student not in submit_student:
        miss_students.append(student)

print(min(miss_students))
print(max(miss_students))