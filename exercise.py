import math

def digits(x):
    return len(list(x))
 
def count_words(x):
    return len(x.split(" "))

def largest(x):
    biggest = x[0]
    for i in x:
       if i > biggest:
           biggest = i
    return biggest

def smallest(x):
    s = x[0]
    for i in x:
       if i < s:
        s = i
    return s

def largest_smallest(x):
    s = b = x[0] # smallest and biggest are set to the first element
    for i in x:
        if i > b:
            b = i
        if i < s:
            s = i
    return s, b


def mean(x):
    acc = 0
    for i in x:
        acc += i
    return acc/len(x)


def median(x):
    c = x[:]
    c.sort() # Sorting x directly modifies the input. This might not be acceptable
    l = len(x) # Calculate this once. Don't repeat the computation
    if l % 2 == 0: # Even number of elements. Average of two middle elements
        mid = math.floor(l/2) # Prefer using math.floor and math.ceil rather than int (more explicit)
        ret = (c[mid]+c[mid-1])/2.0
    else:
        mid = math.floor(l/2)
        ret = c[mid]
    return ret

def tables(x, y):
    for i in range(1, y+1):
        print (f"{x} x {i} = {x*i}")

    # i = 1
    # while  i <= int(y): # Remove superfluous 
    #     k = int(x) * int(i) # calls to "int" 
    #     a = print(f"{x} x {i}= {k}")
    #     i += 1

def tables2(x):
    for c in range(1, x+1):
        row = []
        for r in range(1, x+1):
            row.append("{:5}".format(c*r))
        print (" ".join(row) + "\n")
        
            
    
       # b = 1
       # while b <= x:
       #        for a in range(1,int(x + 1)):
       #               print(a * b, end="\t ")
       #        print('\n')
       #        if b == 1:
       #               print("--+-","-" * 8 * (int(x - 1)))
       #        print('\n')
       #        b += 1
       # return
       
def panagram(x):
    for i in "abcdefghijklmnopqrstuvwxyz": # For each letter
        if i not in x: # If it's missing
            return False # x is not a panagram
    return True # Otherwise all letters are there and it is a panagram
        

    # x =  x.replace(" ", "")
    # a = list(x)
    # b = list(set(a))
    # b.sort()
    # c = "abcdefghijklmnopqrstuvwxyz"
    # d = list(c)
    # if b != d:
    #     return False
    # else:
    #     return True

def freq(s):
    a = list(s)
    a.sort()
    inwords = (set(a))
    new = []
    for word in inwords:
        counts = s.count(word)
        new.append(counts)
    freqdict = {}
    for key in inwords:
        for value in new:
            freqdict[key] = value
            new.remove(value)
            break

    return freqdict

def mode(s):
    inwords = (set(s))
    new = []
    for word in inwords:
        counts = s.count(word)
        new.append(counts)
    freqdict = {}
    for key in new:
        for value in inwords:
            freqdict[key] = value
            inwords.remove(value)
            break

    return  freqdict[max(freqdict.keys())]

def den(x):
    a = 0
    while x >= 2000:
        x -= 2000
        a += 1
        print(f"2000 x {a} = {2000 * a} ({x} left)")
    a = 0
    while x >= 500:
        x -= 500
        a += 1
        print(f"500 x {a} = {500 * a} ({x} left)")
    a = 0
    while x >= 200:
        x -= 200
        a += 1
        print(f"200 x {a} = {200 * a} ({x} left)")
    a = 0
    while x >= 100:
        x -= 100
        a += 1
        print(f"100 x {a} = {100 * a} ({x} left)")
    a = 0
    while x >= 50:
        x -= 0
        a += 1
        print(f"50 x {a} = {50 * a} ({x} left)")
    a = 0
    while x >= 20:
        x -= 20
        a += 1
        print(f"20 x {a} = {20 * a} ({x} left)")
    a = 0
    while x >= 10:
        x -= 10
        a += 1
        print(f"10 x {a} = {10 * a} ({x} left)")
    a = 0
    while x >= 5:
        x -= 5
        a += 1
        print(f"5 x {a} = {5 * a} ({x} left)")
    a = 0
    while x >= 1:
        x -= 1
        a += 1
        print(f"1 x {a} = {1 * a} ({x} left)")
    
    return
