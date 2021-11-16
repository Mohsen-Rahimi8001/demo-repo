# it is a practice of my university
# this program has been written by Mohsen Rahimi.
# it prints the sum of all prime numbers befor two million.

def create_prime(number):
    """ Returns a list of numbers befor number consist of prime numbers and zeros --> [2, 3, 5, 0, 7, 0, ...] """
    
    # numbers between 1 and number
    primary_list = [i for i in range(2, number + 1)]
    
    for i, num in enumerate(primary_list):
        # ignore zeros
        if num == 0:
            continue
            
        # set numbers that are divisible by num to zero.
        index = i + num
        while index < number - 1:
            # Zero is ineffective in add operation and it usefull for adding prime numbers.
            primary_list[index] = 0
            index += num
    
    return primary_list

def sum_of_primes(number):
    #  the sum of all the primes below number.
    res = 0
    for num in create_prime(number):
        res += num
    return res

print(sum_of_primes(2_000_000))