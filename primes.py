from argparse import ArgumentParser 

parser = ArgumentParser()
parser.add_argument('--number', type=int)
args = parser.parse_args()


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):    
        if n % i == 0:
            return False        
    return True

result = isPrime(args.number)
print(f'{args.number} is {"prime" if result else "not prime"}')