file = open("day1.txt", "r")
l = []
for line in file.readlines():
    l.append(line)

value = 50
count = 0
for i in l:
    start = value
    a = int(i[1:])
    if i[0] == 'L':
        value -= a
    else:
        value += a
    # When the rest of euclidian division by 100 differs, add it
    count += abs((start //100 - value // 100))
    # when turning counter-clockwise, we need to refine.
    if i[0] == 'L':
        # If arriving to 0%100, add a click
        if value %100 == 0:
            count += 1
        # If starting from 0%100, remove a click
        if start %100 == 0:
            count -= 1
print("total count", count)
    

