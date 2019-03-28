#coding:utf-8
def pr_triangle(mylist):
    count = sum(mylist)
    length = len(mylist)
    temp = 0
    for i in range(length):
        if count/2 > mylist[i]:
            temp +=1
        else:
            continue
    if temp == length:
        return '任意数小于其他数之和'
    else:
        return '不是任意数小于其他数之和'

mylist = [3,4,5,7,8,10]
print pr_triangle(mylist)

