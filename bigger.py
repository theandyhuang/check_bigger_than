number = int(input("please enter a number: "))
i = 0
sum1 = 0
while True:
    sum1 += i
    if sum1 >= number:
        break
    i += 1
print(f"Summation from 1 to {i} is {sum1} and that is over or equal to {number}")