from argparse import ArgumentParser 

parser = ArgumentParser()
parser.add_argument('--number', type=int)
args = parser.parse_args()


def allPrimesTill(num):
    if num < 0:
        return "Negative numbers cannot be prime"
    elif num < 2:
        return f'{num} cannot be prime'
    else:
        primes = [2]
        for number in range(3, num):
            sqrtNum = number**0.5
            for factor in primes:
                if number % factor ==0:
                    # Not a prime number
                    break
                if factor > sqrtNum:
                    # Prime
                    primes.append(number)
                    break
        return primes    

result = allPrimesTill(args.number)
print(f'For {args.number} found {result if result else "No primes"}')