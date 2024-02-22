print("~~ ICIKIWIR STUDENT GRADER ~~")

n_students = int(input("How many students do you have: "))

grade = dict()

for i in range(n_students):
    print(f"\nStudent no. {i+1}")
    name = input("Name: ")
    score = int(input("Score: "))
    grade[name] = score

print("\nFinal Result:")
print(grade)