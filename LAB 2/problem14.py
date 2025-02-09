marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))
marks3 = int(input("Enter marks for subject 3: "))
total = marks1 + marks2 + marks3
average = total / 3
if marks1 > 39 and marks2 > 39 and marks3 > 39:
    result = "Passed"
else:
    result = "Failed"
if marks1 <= 39:
    grade1 = "F"
elif marks1 <= 44:
    grade1 = "P"
elif marks1 <= 49:
    grade1 = "C"
elif marks1 <= 54:
    grade1 = "B"
elif marks1 <= 59:
    grade1 = "B+"
elif marks1 <= 69:
    grade1 = "A"
elif marks1 <= 79:
    grade1 = "A+"
else:
    grade1 = "O"
if marks2 <= 39:
    grade2 = "F"
elif marks2 <= 44:
    grade2 = "P"
elif marks2 <= 49:
    grade2 = "C"
elif marks2 <= 54:
    grade2 = "B"
elif marks2 <= 59:
    grade2 = "B+"
elif marks2 <= 69:
    grade2 = "A"
elif marks2 <= 79:
    grade2 = "A+"
else:
    grade2 = "O"
if marks3 <= 39:
    grade3 = "F"
elif marks3 <= 44:
    grade3 = "P"
elif marks3 <= 49:
    grade3 = "C"
elif marks3 <= 54:
    grade3 = "B"
elif marks3 <= 59:
    grade3 = "B+"
elif marks3 <= 69:
    grade3 = "A"
elif marks3 <= 79:
    grade3 = "A+"
else:
    grade3 = "O"
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Result: {result}")
print(f"Grades: Subject 1 - {grade1}, Subject 2 - {grade2}, Subject 3 - {grade3}")