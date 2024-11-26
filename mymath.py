def first_n_primes(n):
    if n == 0:
        return []
    primes = [2]
    i = 3
    while len(primes) < n:
        for prime in primes:
            if i % prime == 0:
                break
        else:
            primes.append(i)
            if len(primes) == n:
                return primes
        i += 2
    return primes

def gcd(a, b):
    d = a % b
    while d != 0:
        a = b
        b = d
        d = a % b
    return b


def flystraight(n):
    current = 1
    print(current)
    for i in range(2, n + 1):
        divisor = gcd(i, current)
        if divisor != 1:
            current = current / divisor
        else:
            current = current + i + 1
        print(current)


def wisteria(n):
    for i in range(1, n + 1):
        product = 1
        for digit in str(i):
            product *= int(digit)
        print(i - product)

def hofstadter(n):
    if n < 2:
        return 1
    return hofstadter(n - hofstadter(n - 1)) + hofstadter(n - hofstadter(n - 2))


def prime(n):
    primes = first_n_primes(n)
    with open("prime.txt", "w") as f:
        for prime in primes:
            f.write(str(prime) + "\n")
        f.close()


#It takes an s string and selects the vowels from it, then stores the vowels and the number of occurrences in a dictionary.
def vowel(s):
    vowel_dict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    for char in s:
        if char in vowel_dict:
            vowel_dict[char] += 1
    return vowel_dict
