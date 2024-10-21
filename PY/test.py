# if __name__ == '__main__':
#     N = int(input())
#     ls = [[]]
#     for i in range(0, N + 1):
#         ls[i][0], ls[i][1], ls[i][2] = input().split
#     print(ls)




# import math
# ls = []
# result = []
# N = int(input())
# for i in range(N):
#     ls.append((list(input().split())))
# for i in range(N):
#     if ls[i][0] == "append" :
#         result.append(int(ls[i][1]))
#     if ls[i][0] == "insert" :
#         result.insert(int((ls[i][1])), int((ls[i][2])))
#     if ls[i][0] == "pop" :
#         result.pop()
#     if ls[i][0] == "reverse" :
#         result = result[::-1]
#     if ls[i][0] == "print":
#         print(result)
#     if ls[i][0] == "remove":
#         for j in range(len(result)):
#             if result[j] == int(ls[i][1]):
#                 result.remove(result[j])
#                 break
#     if ls[i][0] == "sort" :
#         result.sort()


# if __name__ == '__main__':
#     n = int(input())
#     integer_list = list(map(int, input().split()))
#     t = ()
#     z = list(t)
#     for i in range(n):
#         z.append(integer_list[i])
#     t = tuple(z)
#     print(hash(t))



# def swap_case(s):
#     re = ''
#     for i in range(len(s)):
#         if s[i] == s[i].lower():
#             re = re + s[i].upper()
#         elif s[i] == s[i].upper():
#             re = re + s[i].lower()
#     return re

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)


# def swap_case(s):
#     re = ''
#     for i in range(len(s)):
#         if s[i] == s[i].lower():
#             re = re + s[i].upper()
#     return re

# s = input()
# result = swap_case(s)
# print(result)

# word = input()
# char = input()

# count = 0
# for i in range(len(word)):
#     if word[i] == char:
#         count += 1
# result = (count/len(word)) * 100
# print(round(result, 3))

# a, b, c = map(int, input().split())

# if (a + b <= c) or (a + c <= b) or (b + c <= a):
#     print("NO")
# else:
#     print("YES")

# import numpy

# print(numpy .abs(-5))

# n = int(input())
# ls = input().split()
# l = int(input())
# m = int(input())

# rs = []
# for i in range(n):
#     if l <= int(ls[i]) <= m:
#         rs.append(ls[i])
# if len(rs) == 0:
#     print("-1")
# else:
#     for i in range(len(rs)):
#         print(rs[i], end = " ")


# ar = [1, 2, 3, 4]
# for i in range(len(ar)):
#     print(ar[i], end = " ")

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)