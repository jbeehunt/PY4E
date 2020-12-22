name = input("Enter file: ")
if len(name) < 1 : name = "mbox.txt"
handle = open(name)
people = dict()
for line in handle:
    words = line.split()
    #print(words)
    for word in words:
        if word != 'From': 
            continue
        else:
            people[words[1]] = people.get(words[1], 0) + 1
      

largest = -1
theword = None
for k,v in people.items():
    #print(k,v)
    if v > largest:
        largest = v
        theword = k
print('There are', largest, 'comments by', theword)

  

  
