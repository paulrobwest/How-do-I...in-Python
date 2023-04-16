# Manual code for 3 basic stats calcs
# Mean - average val for set of numbers. Sum/total num of vals

numbers = [3,6,8,90,21,24,56,1,2,43,22,23,24,25,26,31,22]
mean = sum(numbers)/len(numbers)
print(mean)

# Median - middle value from sorted values. Depends if tot number of vals is odd or even

numbers.sort()

if len(numbers) % 2 == 0:
    m1 = numbers[len(numbers)//2]
    m2 = numbers[len(numbers)//2 - 1]
    median = (m1 + m2)/2
else:
    median = numbers[len(numbers)//2]

print(median)

# Mode - most feq occurring value among values list

frequency = {}
for i in numbers:
    frequency.setdefault(i, 0)
    frequency[i] += 1
print(frequency)

mostfreq = max(frequency.values())
for i, j in frequency.items():
    if j == mostfreq:
        mode = i

print(mode)



