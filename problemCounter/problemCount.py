count = 0
while True:
    problems = (input("Enter Problem String: "))
    groups = problems.split(',')
    #print(groups)
    numbers = []

    for group in groups: 
        numbers.append(group.split('-'))

    #print(numbers)
    
    for num in numbers:
        if (len(num) > 1):
            count += int(num[1]) - int(num[0]) + 1
        else:
            count += 1

    print("Number of Problems: ", count)