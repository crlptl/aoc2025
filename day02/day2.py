def is_invalid(i):
    if len(str(i)) %2 == 1:
        result = False
    else:
        if str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:]:
            result = True
        else:
            result = False
    return(result)

print(is_invalid(11))

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
    

