def divs(number):
    l = []
    for k in range(2, number//2 +1):
        if number % k == 0:
            l.append(k)
    l.append(number)
    return(l)

def is_invalid_for_sequence_length(number, sequence_length):
    print(str(number), sequence_length * str(number)[:(len(str(number))//sequence_length)])
    if str(number) == sequence_length * str(number)[:(len(str(number))//sequence_length)]:
        result = True
        print("yy")
    else:
        result = False
    return(result)


def is_invalid(i):
    result = False
    if i < 10:
        result = False
    else:
        divisors = divs(len(str(i)))
        print(divisors)
        for div in divisors:
            if is_invalid_for_sequence_length(i, div):
                print("Found invalid!", i)
                result = True
                break
    return(result)


file = open("day2.txt", "r")
l = ""
for line in file.readlines():
    l = [i for i in line.split(',')]

result = 0
for element in l:
    numbers = element.split('-')
    start = numbers[0]
    end = numbers[1]
    print(start, end)
    for i in range(int(start), int(end)+1):
        if is_invalid(i):
            print("adding", i)
            result += i
            

print(result)

## too high