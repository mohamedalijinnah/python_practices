from argparse import ArgumentParser 

parser = ArgumentParser()
parser.add_argument('--number')
args = parser.parse_args()

def factorial(num):
    # Your code goes here.
    if num==0:
       return 1
    if num > 0:
            return num * factorial(num - 1)
    else:
        return None

if args.number:
    try:
        args.number = int(args.number)
        result = factorial(args.number)
        print(f'The factorial of {args.number} is {result}')
    except ValueError:
        print('Please enter a valid number')
    
    