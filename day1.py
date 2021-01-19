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


#Project Euler Q11: Largest product in a grid

grid = [] #initially I attempted to code a square matrix thhat iterated through the rows and columns but found that was incredibly complicated
gridstr = '''
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
'''.strip()
for line in gridstr.splitlines(): #for statement for the grid
    grid.append([int(number) for number in line.split()])

greatest = 0 #gives us a variable "greatest"
for y, row in enumerate(grid): #for statements that follow set necessary requirements of the question
    for x, col in enumerate(row):
        for x_dir in range(-1, 2):
            for y_dir in range(-1, 2):
                if x_dir == 0 and y_dir == 0: continue #if statement to set requirements
                product = 1
                for i in range(4):
                    x_pos = x + (i * x_dir)
                    y_pos = y + (i * y_dir)
                    if (x_pos < 0 or y_pos < 0): break #after some research I found using break to terminate thhe current loop and resuming execution in the next line to be extremely useful
                    elif (y_pos >= len(grid) or x_pos >= len(row)): break
                    product *= grid[y_pos][x_pos]
                if product > greatest: #fulfills "greatest product of four adjacent numbers"
                    greatest = product 

print(greatest) #prints answer!


#Project Euler Q12: Highly divisible triangular number

n = 28 #this comes from "We can see that 28 is the first triangle number to have over five divisors."
while True: #I'm creating a loop that only breakes if we generate a trianglenumber with 500 divisors
	triangle_number = n*(n+1)/2 #Sum of numbers from 1 to n
	n = n+1 #incrases n
	dictionary = {} #dictionary to store the powers of primes

	i = 2 #begins with 2

	while i <= triangle_number: #for loop to factor
		
		if triangle_number % i == 0: #If 'i' divides the number, then it is a prime factor 
			triangle_number = triangle_number/i #changes num so we wont be stuck in a loop
			if i in dictionary:	#We are storing the value in terms of power of the prime number
				dictionary[i] += 1
			else:
				dictionary[i] = 1
			i -= 1
		i += 1

     #struggling to continue


#Project Euler Q10: Summation of primes (cont'd)

sieve = [True] * 2000000 #Using the sieve methhod, becaue it is decidedly faster to run 2 million prime numbers
def mark(sieve, x): #In the following implementation, a boolean array is used to mark multiples of prime numbers
    for i in range(x+x, len(sieve), x):
        sieve[i] = False
        
for x in range(2, int(len(sieve) ** 0.5) + 1): #for statement to set ranges for our numbers
    if sieve[x]: mark(sieve, x)
    
print (sum(i for i in range(2, len(sieve)) if sieve[i])) #gives us "the sum of all the primes below two million"

#I attempted the sieve method and was successful! It ran wayyy faster than the previous brute force approach.
