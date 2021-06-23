import math

def solve_quadratic(a,b,c):
    if a == 0:
        print ( )
    elif (b*b-4*a*c) < 0:
        print ( )
    elif (-b + math.sqrt(b*b-4*a*c))/(2*a) == (-b - math.sqrt(b*b-4*a*c))/(2*a):
        print ((-b - math.sqrt(b*b-4*a*c))/(2*a))
    else:
        print ((-b + math.sqrt(b*b-4*a*c))/(2*a))
        print ((-b - math.sqrt(b*b-4*a*c))/(2*a))
