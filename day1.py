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


#Project Euler Q7: 10001st prime

def prime(n): #code function to find prime #s
    numberscheck = range(2, int(n**.5) + 1) #set variable numbers to check
    for i in numberscheck: #for loop ends in either true or false
        if n % i == 0:
            return False 
    return True

def primeindex(index): #define a index function 
    n_primes = 1 #sets variables
    n = 2
    while n_primes < index: #whhile loop
        n+=1
        if prime(n):
            n_primes += 1
    return n

print(primeindex(10001)) #find 10 001st prime number


#Project Euler Q8: Largest product in a series

s = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450' #this is the number
n = 0 #set variable
for i in range(0, len(s)-4): #for loop set in range
    p = 1 #sets variable p
    for j in range(i,i+5): #for loop in range
        p = p * int(s[j]) 
    if p > n: n = p #finds "value of this product" (the thirteen adjacent digits in the 1000-digit number that have the greatest product)

print (n) #prints it!


#Project Euler Q9: Special Pythagorean triplet

for a in range(1, 1000): #begins our for loop for variable a in a range (1,1000)
    for b in range(a, 1000): #anothher one for variable b within range (a,1000)
        c = 1000 - a - b #defines c
        if c > 0: #if statement that sets requirements
            if c*c == a*a + b*b: #if state,emt that fulfills requirements of "A Pythagorean triplet is a set of three natural numbers, a < b < c"
                print (a*b*c) #prints products of abc!
        

#Project Euler Q10: Summation of primes

sum = 2 #sets variable

for number in range(3, 2000000): #for loop that sets our range (3, 2000000)
    prime = True
    for x in range(2, number): #for loop within range
        if number % x == 0: #if statement to find whether it is prime or not
            prime = False
    if prime:
        sum += number #sum of primes

print (sum)

#I actually hhave no idea if the code above works as everytime I have tried to run it it's taken so long that I can't tell if my program is crashing
#That being said, this is a trial division code, one that requires going through this loop 2 million times
#I did some research and found somethhing called the Sieve of Eratosthenes? I'll have to look more into it
