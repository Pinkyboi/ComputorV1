from equation_parser import Parser
from solver import Solver
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py \"equation\"")
        exit(1)
    parser = Parser(sys.argv[1])
    parser.parseEquation()
    Solver.solve(parser.equationFactors)
    