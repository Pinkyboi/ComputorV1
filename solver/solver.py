class Solver():

    @staticmethod
    def throwSolverWarning(warningMessage):
        print(f'\x1b[1;37;42m Solver Warning \x1b[0m : {warningMessage}')

    @staticmethod
    def annouceEquation(equationDict, endPower):
        equationString = ""
        for index, (power, factor) in enumerate(equationDict.items()):
            if index != 0:
                equationString += " + " if factor > 0 else " - "
                factor = abs(factor)
            equationString += f"{factor} * X^{power}"
        equationString += " = 0"
        print("Polynomial degree:", endPower)
        print("Reduced form:", equationString)

    @staticmethod
    def solve(equationDict):
        powerList  = [k for k, v in equationDict.items() if v != 0]
        endPower = max(powerList) if len(powerList) else 0
        allPolinomialFactors = {k: equationDict[k] if k in equationDict.keys() else 0 for k in range(endPower + 1)} 
        Solver.annouceEquation(equationDict, endPower)
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
        print(f"The solution is: {(-b / a):.6f}")

    @staticmethod
    def secondDegree(a, b, c):
        delta = (b ** 2) - (4 * a * c)
        if delta == 0:
            print(f"Discriminant is null the solution is: {(-b / (2 * a)):.6f}")
        else: 
            if delta > 0:
                print("Discriminant is strictly positive, the two solutions are:")
                deltaSqrt = Solver.sqrt(delta)
                firstSolution = f'{(-b - deltaSqrt) / (2 * a) :.6f}'
                secondSolution = f'{(-b + deltaSqrt) / (2 * a) :.6f}'
            else:
                print("Discriminant is strictly negative, the two solutions are:")
                imaginaryPart = Solver.sqrt(Solver.abs(delta)) / (2 * a)
                firstImaginaryPart = f" {'+' if imaginaryPart > 0 else '-'} {abs(imaginaryPart):.6f}i"
                secondImaginaryPart = f" {'-' if imaginaryPart > 0 else '+'} {abs(imaginaryPart):.6f}i"
                firstSolution = f'{-b / 2 * a :.6f}' + firstImaginaryPart
                secondSolution = f'{-b / 2 * a :.6f}' + secondImaginaryPart
            print(firstSolution)
            print(secondSolution)

    @staticmethod
    def sqrt(n, l = 0.000001):  
        x = n  
        count = 0 
        while True:
            count += 1 
            root = 0.5 * (x + (n / x))  
            if (abs(root - x) < l) : 
                break   
            x = root 
        return root 

    @staticmethod
    def abs(x):
        return x if x >= 0 else -x
