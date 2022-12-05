# #Pawan Singh B66
# def rank_of_student(name, mark, updates, n):

#     #list of the student
#     x = [[0 for j in range(3)] for i in range(n)]
#     for i in range(n):

#         # here we store the name of the student
#         x[i][0] = name[i]

#         # here we update the marks of the student
#         x[i][1] = mark[i] +updates[i]

#         #here we store the current rank of the student
#         x[i][2] =i+1

#     maximum = x[0]
#     for j in range(1,n):
#         if (x[j][1] >= maximum[1]):
#             maximum = x[j]

#     #now printing the name and the jump of the student
#     print("Name: ", maximum[0], ", jump:", abs(maximum[2]-1), sep="")


# #calling the function and input values:
# n = int(input("Enter Total Numbers of Students: "))

# name = []
# for i in range(1,n+1):
#     print("Enter the name of student",i,"  ")
#     a = input()
#     name.append(a)
# print(name)

# marks = []
# for i in range(1,n+1):
#     print("Enter the marks of student",i,"  ")
#     b = int(input())
#     marks.append(b)
# print(marks)

# updates = []
# for i in range(1,n+1):
#     print("Enter Updated marks of student",i)
#     c = int(input())
#     updates.append(c)
# print(updates)

# """
# name = ["Satya", "Saurabh", "Suresh"]

# mark = [99,47,69]

# updates = [27, 10, 22]
# """
# n = len(marks)

# rank_of_student(name,marks,updates,n)


a=input()
b=a[-1]
b=int(b)
if b%3==0:
    print("divisible by 3")
else:
    print("not divisible by 3")    