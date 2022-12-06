import re
import sys

class Parser():

    _general_filter = r"[+-]?\d+.?\d*\*[Xx]\^\d"
    _power_filter   = r"[Xx]\^(?P<power>\d)"
    _number_filter  = r"(?<!\^)(?P<sign>[+-])?(?P<number>\d+\.?\d*)"

    def __init__(self, equationString):
        self._equationString = equationString.replace(' ', '')
        self._equationFactors = {}

    def throwParseError(self, errorMessage, token=None):
        if not token:
            print(f'\x1b[1;37;41m Parser Error \x1b[0m : {errorMessage}')
        else:
            print(f'\x1b[1;37;41m Parser Error \x1b[0m : {errorMessage} near \'{token}\'.')
        exit();

    def fillValueList(self, sequence, factor = 1):
        for side in sequence:
            number = float(re.search(self._number_filter, side).group("number"))
            sign = re.search(self._number_filter, side).group("sign")
            power = int(re.search(self._power_filter, side).group("power"))
            if power not in self._equationFactors.keys():
                self._equationFactors[power] = 0
            self._equationFactors[power] += number * factor * (-1 if sign == '-' else 1)
        self._equationFactors = dict(sorted(self._equationFactors.items(), key=lambda item: item[0], reverse=True))

    def parseEquationSides(self):
        equationSides = self._equationString.split('=')
        if len(equationSides) != 2:
            self.throwParseError("Invalid number of sides in equation.")
        for index, equationSide in enumerate(equationSides):
            equationSides[index] = re.findall(self._general_filter, equationSide)
            if not len(equationSides[index]):
                self.throwParseError("Invalid syntax", token = equationSide)
            if ''.join(equationSides[index]) != equationSide:
                self.throwParseError("Invalid syntax", token = equationSide)
        return equationSides

    def parseEquation(self):
        equationSides = self.parseEquationSides()
        self.fillValueList(equationSides[0], factor = 1)
        self.fillValueList(equationSides[1], factor = -1)

    def printEquation(self):
        equationString = ""
        for index, (power, factor) in enumerate(self._equationFactors.items()):
            if index != 0:
                equationString += " + " if factor > 0 else " - "
            equationString += f"{abs(factor)} * X^{power}"
        equationString += " = 0"
        print("Reduced form:", equationString)
            
    @property
    def equationFactors(self):
        return self._equationFactors

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 Parser.py \"<equation>\"")
        exit()
    parser = Parser(sys.argv[1])
    parser.parseEquation()