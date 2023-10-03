from term import Term

class Function:
    def __init__(self, sfunction):
        self.terms = [Term(t) for t in sfunction.split(" ")]
        for term in self.terms:
            if len(term.factor) == 0 and len(term.variable) == 0:
                self.terms.remove(term)
 
    def reorder(self):
        self.terms.sort(key=lambda term: (term.get_power(), term.variable), reverse=True)

    def remove_empty(self):
        for i in range(len(self.terms) - 1, -1, -1):
            term = self.terms[i]
            if int(term.factor) == 0:
                self.terms.pop(i)
        if len(self.terms) == 0: self.terms.append(Term("0"))
        
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
                self.terms[i] += manipulator
                change = True
        if not change: self.terms.append(manipulator)
                   
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
    