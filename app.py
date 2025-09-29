# high_income = True
# good_credit = False

# if high_income and good_credit:
#     print("Eligible for loan")
# else:
#     print("Not eligible for loan")

# leap_year = int(input("Enter a year: "))
# if (leap_year % 4 == 0 and leap_year % 100 != 0) or (leap_year % 400 == 0):
#     print(f"{leap_year} is a leap year")
# else:
#     print(f"{leap_year} is not a leap year")

# sum = 0
# for i in range(0, 20):
#     if i % 2 != 0:
#         sum += list(i)
#         print(sum)
#         print(type(i))

# age = int(input("Enter your age: "))

# if 18 <= age < 65:
#     print("You are eligible to work")
# else:
#     print("You are not eligible to work")


# if 10 == "10":
#     print("a")
# elif "bag" > "apple" and "bag" > "cat":
#     print("b")
# else:
#     print("c")



# if __name__ == '__main__':
#     n = int(input("Enter the Value: ").strip())
#     if n % 2 != 0:
#         print("Weird")
#     elif n % 2 == 0 and 2 <= n <= 5:
#         print("Not Weird")
#     elif n % 2 == 0 and 6 <= n <= 20:
#         print("Weird")
#     elif n % 2 == 0 and n > 20:
#         print("Not Weird")
# success = False
# for i in range(6):
#     # print("attempt", i)
#     if i == 3:
#         print("you have already succeeded", i)
#         break

# for i in range(4):
#     for j in range(3):
#         print(f"({i}, {j})")

# year = int(input("Enter a year: "))
# def is_leap(year):
#     leap = False
#     if year % 4 == 0 and year % 400 == 0 and year % 100 != 0:
#         print("This is leap year")
#         else:
#         print("This is not leap year")
#     # Write your logic here
    
#     return leap
# print(is_leap(year))

# def fizz_buzz():
#     number = int(input("Enter a number: "))
#     if number % 3 == 0 and number % 5 == 0:
#         return f"{number} FizzBuzz"
#     if number % 3 == 0:
#         return f"{number} Fizz"
#     if number % 5 == 0:
#         return f"{number} Buzz"
#     return f"{number} is not divisible by 3 or 5"
# print(fizz_buzz())


# def checkOddEven(x):
#     if x%2==0:
#         print("Even")
#     else:
#         print("Odd")


# checkOddEven(11)
    


# class Solution:
#     def checkStatus(self, a, b, flag):
#         # code here
#         if a>0 and b>=0 and flag is False:
#             return False
#         elif a<0 and b<0 and flag is True:
#             return True

# print(Solution().checkStatus(1, 2, False))


# def cal():
#     print("""press 1: For Addition:
#     press 2: For Subtraction:
#     press 3: For Multiplication:
#     press 4: For Devision:
#     press 5: Exit():""")
#     choice = input("Please Enter the choice according to given instuction: ")
#     # if choice==5:
#     #     print("Exiting the programm")
#     #     exit()
#     velue1=float(input("Please Enter The First Value"))
#     velue2=float(input("Please Enter The Second Value"))    
#     if choice == 1:
#         print("addition of given two value", velue1+velue2)
#     elif choice==2:
#         print("Subtraction of given two value", velue1-velue2)
#     elif choice==3:
#         print("Multiplication of given two value", velue1*velue2)
#     elif choice==4:
#         print("Devision of given two value", velue1//velue2)

        
# cal() 


# letters = ['a', 'b', 'c', 'd']

# letters.pop(0)
# print(letters)

# letter = ["a","b","c","d"]

# print(letter.index("c"))

# letter.append("e")
# letter.insert(0,"-")

# letter.pop(0)
# letter.remove("c")
# del letter[:2]
# print(letter)

# x="1"

# print(type(x))


# list_1 = [1,2,3]
# list_2 = [1,4,5]

# a= list(zip(list_1, list_2))
# print(a)

# def friends_in_trouble(j_angry, s_angry):
#     if j_angry == True and s_angry == True:
#         return True
#     elif j_angry == False and s_angry == False:
#         return False
#     elif j_angry == True and s_angry == False:
#         return False
#     elif j_angry == False and s_angry == True:
#         return False
# print(friends_in_trouble(False, True))


# def eaight_queeen()


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def draw(self):
#         print(f"Point ({self.x}), ({self.y}")
# point = Point(1,2)
# point.draw()

# inp = int(input("Enter of number N to get the prime factors: "))
# def prime_factors(n):
#     i = 2
#     factors = []
#     while i * i <= n:
#         if n % i:
#             i += 1
#         else:
#             n //= i
#             factors.append(i)
#     if n > 1:
#         factors.append(n)
#     return factors 
