import sys

try:
    n = sys.argv[1]
except IndexError:
    n = input("Enter something, yo! ")

while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        n = input("Enter something, yo! ")

print("Fizz buzz counting up to " + str(n))

counter = 0

for counter in range(1,n+1):
    if counter % 3 == 0 and counter % 5 == 0:
        print("fizz buzz")
    elif counter % 3 == 0:
        print("fizz")
    elif counter % 5 == 0:
        print("buzz")
    else:
        print(counter)
        
