#largest so far
largest_so_far = -1
print('before', largest_so_far)
for the_num in [9,41,12,3,74,15] :
    if the_num > largest_so_far :
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('after', largest_so_far)
# Counting
zork = 0
print('before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + 1
    print(zork, thing)
print('after', zork)
#
zork = 0
print('before', zork)
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
    print(zork, thing)
print('after', zork)
#count, sum, average
count = 0
sum = 0
print('before', count, sum)
for value in [9,41,12,3,74,15] :
    count = count +1 
    sum = sum + value
    print(count, sum, value)
print('after', count, sum, sum/count)
#find large number Boolean
print('before')
for value in [9, 41, 12, 3, 74, 15] :
    if value > 20:
        print('Large number', value)
print('After')
found = False
#found, false
print('before', found)
for value in [9,41,12,3,74,15]:
    if value == 3 :
        found = True
    print(found, value)
print('after', found)
#find the smallest value
smallest = None #flag value
print('Before')
for value in [9, 41, 12, 3, 74, 15] :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('after', smallest)
tot = 0
for i in [5, 4, 3, 2, 1] :
    tot = tot +1
print(tot)
n = 0
while n > 0:
    print('lather')
    print('rinse')
print('dry off')

#Example 5.1
#running count and runnung total
num = 0
tot = 0.0
while True :
    sval = input('Enter a number:')
    if sval == 'done' : 
        break
    try:
        fval = float(sval)
    except:
        print('invalid input')
        continue 
    #print(fval)
    num = num + 1
    tot = tot + fval

#print('ALL DONE')
print(tot, num, tot/num)
    