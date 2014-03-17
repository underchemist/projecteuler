# problem 48 from projecteuler [Self powers]

#!/usr/bin/env python


sum = 0;
for i in range(1,1001):
    sum += i**i

print sum % 10000000000