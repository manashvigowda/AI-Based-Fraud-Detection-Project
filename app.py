name = input("Enter student name: ")
m1 = int(input("Enter subject 1 marks: "))
m2 = int(input("Enter subject 2 marks: "))
m3 = int(input("Enter subject 3 marks: "))
m4 = int(input("Enter subject 4 marks: "))
m5 = int(input("Enter subject 5 marks: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5
percentage = total / 500 * 100

print("Student:", name)
print("Total:", total)
print("Average:", average)
print("Percentage:", percentage, "%")