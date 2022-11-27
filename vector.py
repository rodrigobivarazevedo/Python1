a = [1,2,3,4,5]    #first 5 dimension vector
b = [6,7,8,9,10]   #second 5 dimension vector
c = []              #vector to store sum of both

for i in range(len(a)):
    c.append(a[i] + b[i])

print(c)
