#check and count the prime numbers in a given range
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def count_primes_in_range(start, end):
    prime_count = 0
    for number in range(start, end + 1):
        if is_prime(number):
            prime_count += 1
    return prime_count
# Example usage
if __name__ == "__main__":
    start_range = int(input("Enter the start of the range: "))
    end_range = int(input("Enter the end of the range: "))
    count = count_primes_in_range(start_range, end_range)
    print(f"Number of prime numbers between {start_range} and {end_range}: {count}")
