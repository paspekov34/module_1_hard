grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
res = sorted(students)
name0 = res[0]
name1 = res[1]
name2 = res[2]
name3 = res[3]
name4 = res[4]
floats = list(map(float, grades[0]))
floats1 = list(map(float, grades[1]))
floats2 = list(map(float, grades[2]))
floats3 = list(map(float, grades[3]))
floats4 = list(map(float, grades[4]))
import statistics
res_mean0 = statistics.mean(floats)
res_mean1 = statistics.mean(floats1)
res_mean2 = statistics.mean(floats2)
res_mean3 = statistics.mean(floats3)
res_mean4 = statistics.mean(floats4)
floats = list(map(float, grades[0]))
floats1 = list(map(float, grades[1]))
floats2 = list(map(float, grades[2]))
floats3 = list(map(float, grades[3]))
floats4 = list(map(float, grades[4]))
slov = dict([[name0,res_mean0],
            [name1,res_mean1],
            [name2,res_mean2],
            [name3,res_mean3],
            [name4,res_mean4]])
print(slov)













