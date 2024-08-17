grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johhny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(len(grades[0]))
print(sum(grades[0]))
grades[0] = sum(grades[0])/len(grades[0])
print(grades[0])
print(len(grades[1]))
print(sum(grades[1]))
grades[1] = sum(grades[1])/len(grades[1])
print(grades[1])
print(len(grades[2]))
print(sum(grades[2]))
grades[2] = sum(grades[2])/len(grades[2])
print(grades[2])
print(len(grades[3]))
print(sum(grades[3]))
grades[3] = sum(grades[3])/len(grades[3])
print(grades[3])
print(len(grades[4]))
print(sum(grades[4]))
grades[4] = sum(grades[4])/len(grades[4])
print(grades[4])
print(grades)
print(list(students)+grades)
print(sorted(students)+grades)
a = (sorted(students)+grades)
print(a)
a = a[0],a[5],a[1],a[6],a[2],a[7],a[3],a[8],a[4],a[9]
print(a)
print(dict([(a[0],a[1]),(a[2],a[3]),(a[4],a[5]),(a[6],a[7]),(a[8],a[9])]))














































