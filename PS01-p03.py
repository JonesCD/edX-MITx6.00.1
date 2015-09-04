import time
start = time.clock()
import winsound
Freq = 250 # Set Frequency To 2500 Hertz
Dur = 200 # Set Duration To 1000 ms == 1 second
############################
s = 'xlojrhmdwvsoufiskpynyf'

i = 0
length = len(s)
longest = ''


for i in range(length):
	temp = ''
	j = 0
	for j in range(length):
		if s[j] == s[-1]:
			temp += s[j]
			if len(temp) > len(longest):
				longest = temp
			temp = ''
		elif s[j] > s[j + 1]:
			temp += s[j]
			if len(temp) > len(longest):
				longest = temp
			temp = ''
		else:
			temp += s[j]
	
print "Longest substring in alphabetical order is:" + longest
	
############################
end = time.clock()
print 'elapsed time:',end - start
#winsound.Beep(Freq,Dur)
