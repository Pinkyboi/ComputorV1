import re

general_filter = r"[+-]? ?\d+.?\d*? \* [Xx]\^\d"
power_filter   = r"[Xx]\^(?P<power>\d)"
number_filter  = r"(?<!\^)(?P<sign>[+-])? ?(?P<number>\d+.?\d*)"
equation_factors = []

def first_degree(a, b):
    print("the solution is:" + f'{-b/a :.6f}')

def sqrt(n, l) :  
    x = n  
    count = 0 
    while (1) : 
        count += 1 
        root = 0.5 * (x + (n / x))  
        if (abs(root - x) < l) : 
            break   
        x = root 
    return root  

def second_degree(a, b, c):
    delta = (b * b) - (4 * a * c)
    if delta >= 0:
        print("Discriminant is strictly positive, the two solutions are:")
        delta = sqrt(delta, 0.000001)
        first_solution = f'{(-b - delta) / (2 * a) :.6f}'
        second_solution = f'{(-b + delta) / (2 * a) :.6f}'
    else :
        print("Discriminant is strictly negative, the two solutions are:")
        delta = sqrt(abs(delta),0.000001)
        first_solution = f'{-b / 2 * a :.6f}' + "-" + f'{delta / 2 * a:.6f}' + "i"
        second_solution = f'{-b / 2 * a :.6f}' + "+" + f'{delta / 2 * a:.6f}' + "i"
    print(first_solution)
    print(second_solution)

def abs(x):
    return x if x >= 0 else -x

def fill_list_values(sequence, side):
    factor = 1 if side == "right" else -1
    for side in sequence:
        number = float(re.search(number_filter, side).group("number"))
        sign = re.search(number_filter, side).group("sign")
        power = int(re.search(power_filter, side).group("power"))
        while power > len(equation_factors) - 1:
            equation_factors.append(0);
        equation_factors[power] += number * factor * (-1 if sign == '-' else 1)

def equation_cleanup(equation_factors):
    for i in range(len(equation_factors) - 1, -1, -1):
        if(equation_factors[i]):
            break
        else:
            del equation_factors[i]
    
        
def print_equation():
    reduced_equation = ""
    polynomial_degree = len(equation_factors)  - 1
    for index, x in enumerate(equation_factors):
        reduced_equation += ("- " if x < 0 else "" if not reduced_equation else "+ ") + str(abs(x)) + " X^" + str(index) + " "
    reduced_equation += "= 0"
    print("Reduced form:", reduced_equation)
    equation_cleanup(equation_factors)
    polynomial_degree = len(equation_factors)  - 1
    print("Polynomial degree: ", polynomial_degree)
    if polynomial_degree == 2 and equation_factors[2]:
        second_degree(equation_factors[2], equation_factors[1], equation_factors[0])
    elif polynomial_degree == 1 and equation_factors[1]:
        first_degree(equation_factors[1], equation_factors[0])  
    

def equation_recognition():
    sides = input()
    sides = sides.split("=")
    if len(sides) != 2:
        exit();
    right_side  = re.findall(general_filter, sides[0])
    left_side  = re.findall(general_filter, sides[1])
    fill_list_values(right_side, "right")
    fill_list_values(left_side, "left")
    print(equation_factors)
    if equation_factors:
        print_equation()

def main():
    equation_recognition()

if __name__ == "__main__":
    main()