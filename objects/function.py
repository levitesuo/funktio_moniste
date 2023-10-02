from term import Term
from random import randint as r

class Function:
    #This part of the code is for creating and handeling functions.
    #When creating the function there shoud be a space between each term
    #Powers shoud be marked with the ^ character
    #for random numbers use these q = -10 - 10 excluding 0      w = 1 - 10        e = -1 - -10         r = -20_-10 or 20 - 10
    #for numbers to make the solution int use a
    #Accepted variables are x, y and z
    accepted_variables = ["x", "y", "z"]
    def __init__(self, sfunction):
        self.terms = [Term(t) for t in sfunction.split(" ")]

        '''
        left_side_terms = []
        right_side_terms = []
        list_of_terms = sfunction.split(" ")
        on_left_side = True
        
        for term in list_of_terms:
            print("Term: ", term)
            factor = ""
            variable = ""
            at_variable = False
            for i in range(len(term)):
                char = term[i]
                char_out = char
                print("character num ", i, "is: ", char)
                if char == "q" or char == "r":
                    if r(1, 2) == 2: polar = -1
                    else: polar = 1
                    if char == "q": char_out = str(r(1, 10) * polar)
                    else:           char_out = str(r(10, 20) * polar)
                if char == "w": char_out = str(r(1, 10))
                if char == "e": char_out = str(r(-10, -1))
                if  char in self.accepted_variables or ((
                    char == "+" or char == "-") and term[i+1] in self.accepted_variables):
                        at_variable = True
                if char != "=":
                    if at_variable: variable += char_out
                    else:           factor += char_out
                    print("At variable ", at_variable)
                else: on_left_side = False
            final_term = Term(factor, variable)
            print("FTerm: ", final_term.get_latex())
            if on_left_side: left_side_terms.append(final_term)
            else: right_side_terms.append(final_term)                
            self.left_side_terms = left_side_terms
            self.right_side_terms = right_side_terms
            '''
 
    def reorder(self):
        self.terms.sort(key=lambda term: term.get_power(), reverse=True)

    def remove_empty(self):
        for i in range(len(self.terms) - 1, 0, -1):
            term = self.terms[i]
            if int(term.factor) == 0:
                self.terms.pop(i)
        
    def get_latex(self):
        self.reorder()
        self.remove_empty()
        output = ""
        for i in range(len(self.terms)):
            term = self.terms[i]
            if i == 0: output += term.get_latex().replace("+", "")
            else: output += term.get_latex()
        return output
            
    def manipulate_add(self, termstr):
        manipulator = Term(termstr)
        change = False
        for i in range(len(self.terms)):
            if self.terms[i].variable == manipulator.variable:
                self.terms[i] + manipulator
                change = True
        if not change: self.terms.append(manipulator)
    
    #def manipulate_mul(self, termstr):
                   
if __name__ == "__main__":
    f = Function("4y 5x 11")
    print(f.get_latex())
    f.manipulate_add("-4")
    print(f.get_latex())
    f.manipulate_add("3")
    print(f.get_latex())
    f.manipulate_add("3x")
    print(f.get_latex())
    f.manipulate_add("-10")
    print(f.get_latex())