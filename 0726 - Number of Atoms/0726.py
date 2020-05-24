# Not finished
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        elements = {}
        queue = []
        for i, s in enumerate(formula):
            if s == '(':
                temp = {}
            if s == ')':

            # Check if letter is caps, i.e. element
            if s.isupper():
                if s[i+1].islower():
                    element = s[i:i+1]
                else:
                    elemenet = s
                if element not in elements:
                    elements[element] = 1
