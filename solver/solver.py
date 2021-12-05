
def firstDegree(a, b):
    print("the solution is:")
    print(-b/a)

def secondDegree(a, b, c):
    delta = (b * b) - (4 * a * c)
    if delta == 0:
        print("Discriminant is null the solution is:")
        print((-b) / (2 * a))
    else : 
        if delta > 0:
            print("Discriminant is strictly positive, the two solutions are:")
            delta = sqrt(delta)
            first_solution = f'{(-b - delta) / (2 * a) :.6f}'
            second_solution = f'{(-b + delta) / (2 * a) :.6f}'
        else :
            print("Discriminant is strictly negative, the two solutions are:")
            delta = sqrt(abs(delta))
            first_solution = f'{-b / 2 * a :.6f}' + " - " + f'{delta / 2 * a:.6f}' + "i"
            second_solution = f'{-b / 2 * a :.6f}' + " + " + f'{delta / 2 * a:.6f}' + "i"
        print(first_solution)
        print(second_solution)

def sqrt(n, l = 0.000001) :  
    x = n  
    count = 0 
    while (1) : 
        count += 1 
        root = 0.5 * (x + (n / x))  
        if (abs(root - x) < l) : 
            break   
        x = root 
    return root 

def abs(x):
    return x if x >= 0 else -x