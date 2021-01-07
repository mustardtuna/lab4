#Project Euler Q1: Multiples of 3 and 5

total_sum = 0 #establishing variable equivalent to 0
for i in range(1000): #for statement using range function in order to complete the requirement of "below 1000" written in the problem
    if (i%3 == 0 or i%5 == 0): #setting requirements for "multiples of 3 or 5"
        total_sum = total_sum+i #adds sum of all these numbers together 
print(total_sum) #returns total_sum!


#Project Euler Q2: Even Fibonacci numbers

#class Euler(): #tried to write a function here to simplify my code, didnt work.
    #def divisible(limit, divs):
        #return (i for i in  range(limit) if any(i % div == 0 for div in divs))
#print(sum divisible(1000, (3, 5)))

fib = 1 #setting variables, establishing the first 2 fibonacci numbers
fib2 = 2
hold = 0 #basically extra variable to hold the results
total = 0 #total is currently 0

while hold <=4000000: #establishes the "considering the terms in the Fibonacci sequence whose values do not exceed four million" part of the question
    hold = fib2 #equating hold to second number in fibonacci sequence
    if hold % 2 == 0: #begins process of finding fibonacci numbers, finds evens
        total += hold
    hold = fib + fib2 #switches values around for our variables to find the total
    fib = fib2
    fib2 = hold

print(total) #returns total!


#Project Euler Q3: Largest prime factor

n = 600851475143 #establishes requirements of question using a variable; "What is the largest prime factor of the number 600851475143?"
i = 2 #establishes variable i 
while i * i < n: #while loop
    while n % i == 0: #another wihle loop
        n = n / i #n is equivalent to n/i
    i = i + 1 

print (n) #prints n, gives us answer to the largest prime factor question!


#Project Euler Q4: Largest palindrome product

n = 0 #establishes base necessary for finding palindrome product!
for a in range(999, 100, -1): #sets our ranges for a
    for b in range(a, 100, -1): #sets our ranges for b
        x = a * b #formula for product
        if x > n: #if statement
            s = str(a * b)
            if s == s[::-1]:
                n = a * b   #completes palindrome product requirements

print (n) #prints answer!


#Project Euler Q5: Smallest multiple

def gcd(a,b): return b and gcd(b, a % b) or a #establishes element greatest common denominator
def lowestcommonmult(a,b): return a * b / gcd(a,b) #establishes lowest common multiples

n = 1 #sets n as main variable
for i in range(1, 20): #parameteres for "evenly divisible by all of the numbers from 1 to 20"
    n = lowestcommonmult(n, i) #asks n to use lowestcommonmult to find the smallest multiple

print (n) #prints answer!


#Project Euler Q6: Sum square difference

#this one was deceptively simple. I knew it had something to do with a pattern so I tried to establish set variables in my code initially. didn't work so I moved onto this.
def sumsquaredifference(n): #establishes function
      return (((n**2) * (n + 1)**2) / 4) - (n * (n + 1) * (2*n + 1) / 6) #formula for the pattern

print(sumsquaredifference(100)) #prints out answer to "Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."
