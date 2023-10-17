print("this is my second try")
x = 1 
print (x)
Name = input('enter file:')
handle = open(name)
counts = dict ()
for line in handle:
        words = line.split ()
        for word in words:
            counts[word] = counts.get(word,0) + 1
Bigcount = none
bigword = none
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = count
        bigcount = count