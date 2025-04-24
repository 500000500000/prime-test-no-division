
# Start the table of squares, which will grow as needed within get_square().
# The table of odd numbers is just to support the table of squares,
# so that the function get_square() uses only additions.
# For example 1 + 3 + 5 + 7 = 16.
square_table = [0, 1, 4, 9, 16]
odd_table = [1, 3, 5, 7, 9]

# Return i*i without doing any multiplications.
def get_square(i):
    if i >= len(square_table):
        square_table.append(square_table[i-1] + odd_table[i-1])
        odd_table.append(odd_table[i-1] + 2)
    return square_table[i];
  
# Return true if n is an odd prime number.
# The algorithm requires no divisions, multiplications, square roots or differences, just additions.
# Limitations:
# The input n must be odd.
# The function incorrectly reports that 1 is prime.
def is_prime(n):
    i = 0
    j = 1
    while True:
        si = get_square(i)
        sj = get_square(j)
        if si + n > sj:
            j = j + 1
        elif si + n < sj:
            i = i + 1
        else:
            break;
    if i + 1 == j:
        return True
    else:
        return False    
    
# Given an odd number n, call is_prime(n).
# If the result is true, print "<n> is prime."    
def test_is_prime(n):
    if is_prime(n):
        print(n," is prime.") 
        
# MAIN
def main():
    # Print all odd primes less than 1000,
    # including (incorrectly) 1.
    for n in range(1, 1000, 2):
        test_is_prime(n) 
        
# ENTRY POINT
main()