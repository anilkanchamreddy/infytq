#PF-Exer-38
#This verification is based on string match.
import math

num1=36
num2=7
num3=18

calc = lambda num1,num2:(num1%num2)+(num1-num2)#Write the lambda expression for question1
print(calc(num1,num2))

square_root = lambda num3:math.sqrt(num3)#Write the lambda expression for question2
print(square_root(num3))

square_root2=lambda num3:num3**0.5 #Write the lambda expression for question3
print(square_root2(num3))
