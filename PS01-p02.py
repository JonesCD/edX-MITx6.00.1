numBobs = 0
numCons = 0
#s = 'noavvnebobbobobnaiovnaa'

for char in range(0, len(s), 1):
    if s[char:char + 3] == 'bob':
        numBobs += 1


print 'Number of times bob occurs is: ' + str(numBobs)
# print 'numCons is: ' + str(numCons) 
