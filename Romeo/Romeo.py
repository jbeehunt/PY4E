fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    for word in line.split():
        if word in lst:
            pass
        else:
            lst.append(word)
    lst.sort()

print(lst)        
#print(line.rstrip())