

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count = 0
total = 0
fh = open(fname)
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    sb = line.split()
    sc = sb[1]    # this gaves me the numbers only from eavh line #
    value = float(sc)
    total = total + value

if count:
    average = total / count
    print('Average spam confidence:', average)