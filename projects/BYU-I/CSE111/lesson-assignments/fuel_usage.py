import os
def main():
    start = float(input('What was the starting odometer in miles? '))
    end = float(input('What is ending odometer in miles? '))

    fuel = float(input('How much fuel was used, in gallons? '))
    mpg = miles_per_gallon(start, end, fuel)
    lp100k = lp100k_from_mpg(mpg)
    print(f'Miles Per Gallon: {mpg:.1f}{os.linesep}Liters Per 100 Kilometers: {lp100k:.2f}')

def miles_per_gallon(start, end, fuel):
    total = end - start
    return total / fuel
def lp100k_from_mpg (mpg):
    return (235.214583 / mpg)

main()