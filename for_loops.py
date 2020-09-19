friends = ["Bob", "Ane", "Kevin", "John"]

for friend in friends:
    print(f"{friend} is my friend!")

grades = [10, 50, 60, 80, 15.67]
# to find the sum you could use SUM(grades) instead of using for loop
sum_grades = 0
length_grades = len(grades)

for grade in grades:
    sum_grades += grade

average = sum_grades / length_grades

print(f"Average of grades is: {average:.2f}")
