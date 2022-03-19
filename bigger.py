number = int(input("please enter a number: "))
sum1 = 0
for i in range(number):
    sum1 += i
    if sum1 >= number:
        break
print(f"Summation from 1 to {i} is {sum1} and that is over or equal to {number}")