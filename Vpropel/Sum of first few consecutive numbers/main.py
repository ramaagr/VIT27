#codex

#SUM OF FIRST FEW CONSECUTIVE PRIME NUMBERS
'''Sum of First Few Consecutive Prime Numbers
Given a number 'n', write an algorithm and a code to check if it can be written as sum of first few prime numbers. Print Yes if 'n' can be written as first few prime numbers and No otherwise. For example, if n is 5 then print Yes as it can be written as 2+3, if n is 41 then print Yes as it can be written as 2 + 3 + 5 + 7 + 11 + 13 and if n is 11 then print 'No' as it cannot be written as sum of first few prime numbers.

Input Format

First line contains the number, n

Output Format

First line contains Yes if the number n can be written as sum of first few prime numbers and No otherwise'''


#code :

def isprime(i):
    for j in range(2,(i//2+1)):
        if i % j == 0:
            return False
    else:
        return True

n = int(input())
sum = 0
i = 1

while sum<n:
    for k in range( i+1 , n+1):
        if isprime(k):
            sum += k
            i = k
            break
    else:print('it ended')
else:
    if sum == n:
        print('Yes')
    else:
        print('no')
    
