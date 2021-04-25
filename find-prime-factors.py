def get_prime_factors(input):
    factors = []
    for divisor in range (2,input):
        if input % divisor == 0:
            factors.append(divisor)
            input /= divisor
    if len(factors) == 0:
        factors.append(input)
    return factors

print(get_prime_factors(5))