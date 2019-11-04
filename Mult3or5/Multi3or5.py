""" 
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000. 
"""

max_num = 1000
a = 3
b = 5
n_a = 0
n_b = 0
the_sum = 0

for i in range(1, max_num):
    n_a = a*i
    if n_a < max_num:
        the_sum += n_a
        #print('3 mult: ', n_a)
    n_b = b*i
    if n_b < max_num:
        the_sum += n_b
        #print('5 mult: ', n_b)

print(the_sum)

"""
O(n)
import time
timer = time.time()
ans = 0
for i in range(1,1000):
    if i%3==0 or i%5==0:
        ans+=i
print ans
print "Completed in "+str(time.time()-timer)+" seconds."

O(1)
import time
timer = time.time()
ans = 0
mult3 = 333
mult5 = 199
mult15 = int(1000/15)
print 3*mult3*(mult3+1)/2 + 5*mult5*(mult5+1)/2 - 15*mult15*(mult15+1)/2
print "Completed in "+str(time.time()-timer)+" seconds." 

"""
