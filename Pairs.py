# Enter your code here. Read input from STDIN. Print output to STDOUT
line = raw_input()
n, k = (int(s) for s in line.split())
line = raw_input()
z = set()
for s in line.split():
    z.add(int(s))
counter = 0
for s in z:
    if s + k in z:
        counter += 1
print counter
    
    
#y = set([])
#for s in z:
#    y.add(s + k)
#x = set.intersection(z, y)
#print len(x)