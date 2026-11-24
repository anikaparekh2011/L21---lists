empty_list = []
marks_list = [23, 34, 45, 56, 12]
print(marks_list)
print(len(marks_list))

print(marks_list[0])
print(marks_list[1])
print(marks_list[2])
print(marks_list[-1])
print(marks_list[-2])

marks_total = marks_list[0] + marks_list[1] + marks_list[2] + marks_list[-1] + marks_list[-2]
print(marks_total)

marks_average = marks_total / len(marks_list)
print(marks_average)