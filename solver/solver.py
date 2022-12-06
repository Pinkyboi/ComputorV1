class Solver():

    @staticmethod
    def throwSolverWarning(warningMessage):
        print(f'\x1b[1;37;41m Solver Warning \x1b[0m : {warningMessage}')

    @staticmethod
    def solve(equationDict):
        endPower = max(equationDict.keys())
        allPolinomialFactors = {k: equationDict[k] if k in equationDict.keys() else 0 for k in range(endPower + 1)} 
        if endPower == 0:
            if allPolinomialFactors[0] == 0:
                print("Every real number is a solution !")
            else:
                Solver.throwSolverWarning("There is no solution !")
        elif endPower == 1:
            Solver.firstDegree(allPolinomialFactors[1], allPolinomialFactors[0])
        elif endPower == 2:
            Solver.secondDegree(allPolinomialFactors[2], allPolinomialFactors[1], allPolinomialFactors[0])
        else:
            Solver.throwSolverWarning("The polynomial degree is stricly greater than 2, I can't solve.")

    @staticmethod
    def firstDegree(a, b):
        print(f"the solution is: {(-b / a):.6f}")

    @staticmethod
    def secondDegree(a, b, c):
        delta = (b * b) - (4 * a * c)
        if delta == 0:
            print(f"Discriminant is null the solution is: {(-b / (2 * a)):.6f}")
        else: 
            if delta > 0:
                print("Discriminant is strictly positive, the two solutions are:")
                deltaSqrt = Solver.sqrt(delta)
                first_solution = f'{(-b - deltaSqrt) / (2 * a) :.6f}'
                second_solution = f'{(-b + deltaSqrt) / (2 * a) :.6f}'
            else:
                print("Discriminant is strictly negative, the two solutions are:")
                deltaSqrt = Solver.sqrt(Solver.abs(delta))
                first_solution = f'{-b / 2 * a :.6f}' + " - " + f'{deltaSqrt / 2 * a:.6f}' + "i"
                second_solution = f'{-b / 2 * a :.6f}' + " + " + f'{deltaSqrt / 2 * a:.6f}' + "i"
            print(first_solution)
            print(second_solution)

    @staticmethod
    def sqrt(n, l = 0.000001):  
        x = n  
        count = 0 
        while (1) : 
            count += 1 
            root = 0.5 * (x + (n / x))  
            if (abs(root - x) < l) : 
                break   
            x = root 
        return root 
    
    @staticmethod
    def abs(x):
        return x if x >= 0 else -x
