import re
import sys
import solver

general_filter = r"[+-]? ?\d+.?\d*? \* [Xx]\^\d"
power_filter   = r"[Xx]\^(?P<power>\d)"
number_filter  = r"(?<!\^)(?P<sign>[+-])? ?(?P<number>\d+.?\d*)"

def fillValueList(equation_factors, sequence, side):
    factor = 1 if side == "right" else -1
    for side in sequence:
        number = float(re.search(number_filter, side).group("number"))
        sign = re.search(number_filter, side).group("sign")
        power = int(re.search(power_filter, side).group("power"))
        while power > len(equation_factors) - 1:
            equation_factors.append(0);
        equation_factors[power] += number * factor * (-1 if sign == '-' else 1)

def equationCleanUp(equation_factors):
    for i in range(len(equation_factors) - 1, -1, -1):
        if(equation_factors[i]):
            break
        else:
            del equation_factors[i]

def printReducedForm(equation_factors):
    reduced_equation = ""
    for index, x in enumerate(equation_factors):
        reduced_equation += ("- " if x < 0 else ("" if not reduced_equation else "+ ")) + str(abs(x)) + " * X^" + str(index) + " "
    reduced_equation += "= 0"
    print("Reduced form:", reduced_equation)

def print_equation(equation_factors):
    printReducedForm(equation_factors)
    equationCleanUp(equation_factors)
    polynomial_degree = len(equation_factors)  - 1
    if polynomial_degree == -1:
        print("All real numbers are a solution to this polynomial");
    elif polynomial_degree == 0:
        print("There is no solution for this polynomial")
    elif polynomial_degree == 1:
        print("Polynomial degree:", polynomial_degree)
        solver.firstDegree(equation_factors[1], equation_factors[0])
    elif polynomial_degree == 2:
        print("Polynomial degree:", polynomial_degree)
        solver.secondDegree(equation_factors[2], equation_factors[1], equation_factors[0])
    else:
        print("The polynomial degree is stricly greater than 2, I can't solve.")

def throwError(errorMessage):
    print('\x1b[6;30;41m Error \x1b[0m : ' + errorMessage)
    exit();

def checkTrailingChar(regexSet, mainSet):
    for element in regexSet:
        mainSet = mainSet.replace(element, "", 1)
    mainSet = mainSet.replace(' ', "")
    if len(mainSet):
        throwError("Unknown trailing character")


def equation_recognition(sides):
    equation_factors = []
    sides = sides.split("=")
    if len(sides) != 2:
        throwError("Wrong polynomial format");
    right_side  = re.findall(general_filter, sides[0])
    left_side  = re.findall(general_filter, sides[1])
    checkTrailingChar(right_side, sides[0])
    checkTrailingChar(left_side, sides[1])
    if (not len(right_side) or not len(left_side)) : 
        throwError("Wrong polynomial format")
    fillValueList(equation_factors, right_side, "right")
    fillValueList(equation_factors, left_side, "left")
    if equation_factors:
        print_equation(equation_factors)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        equation_recognition(sys.argv[1])