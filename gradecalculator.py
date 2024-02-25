# aking input
bangla_mark = float(input("Bangla Marks: "))
english_mark = float(input("English Marks: "))
math_mark = float(input("Math Marks: "))
science_mark = float(input("Science Marks: "))


average_mark = (bangla_mark + english_mark + math_mark + science_mark) / 4

# Grade
if average_mark >= 91:
    grade = 'A+'
elif average_mark >= 81:
    grade = 'A'
elif average_mark >= 71:
    grade = 'B'
elif average_mark >= 61:
    grade = 'C'
elif average_mark >= 41:
    grade = 'D'
else:
    grade = 'F'

print("Total Grade: ", grade)
