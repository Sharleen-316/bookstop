d = {}
with open("books.txt") as f:
    for line in f:
        (key, val) = line.split()
        d[int(key)] = val

print (d)