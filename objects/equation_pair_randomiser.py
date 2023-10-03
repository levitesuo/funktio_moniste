from equation_group import Equation_group
#from get_random import get_nonzero_random as r
from random import randint
def r(range_start, range_end):
        out = randint(range_start, range_end)
        while out == 0: out = randint(range_start, range_end)
        return out

def get_equation_pair_xy_method():
    solution = (r(-10, 10), r(-10, 10))
    x_factor = r(-10, 10)
    y_factor = r(-10, 10)
    x_constant = solution[1] - x_factor*solution[0]
    y_constant = solution[0] - y_factor*solution[1]
    return Equation_group([f"{x_factor}x {x_constant} = 1y", 
                            f"{y_factor}y {y_constant} = 1x"])

def get_equation_pair_xy_method_scrambeld():
    eq = get_equation_pair_xy_method()
    for i in range(2):
        eq.manipulate_add(i, str(r(-5, 5))+"x")
        eq.manipulate_add(i, str(r(-5, 5))+"y")
        eq.manipulate_add(i, str(r(-10, 10)))
    
    return eq
    
def get_smart_scramble_equation_for_sub():
    eq = get_equation_pair_xy_method()
    eq.manipulate_add(0, "-1y")
    eq.manipulate_add(1, "-1x")
    manipulators = []
    for i in range(2):
         for term in eq.equations[i].left.terms:
              if len(term.variable) == 0:
                   manipulators.append(term.factor)
    print(manipulators)
    for i in range(2):
        eq.manipulate_add(i, str(int(manipulators[i])*-1))
    return eq

def get_good_sub_equation():
    #a1x + b1y = c1
    #a2x + b2y = c2
    a1 = 1
    b1 = 1
    a2 = 1
    b2 = 1
    while a1/b1 == a2 / b2:
        range = 9
        solution = (r(range * -1, range), r(range * -1, range))
        
        y_axel1 = r(range * -1, range)
        x_axel2 = r(range * -1, range)

        c1 = y_axel1 * solution[0]
        c2 = x_axel2 * solution[1]
        
        b1 = solution[0]
        a1 = y_axel1 - solution[1]
        
        a2 = solution[1]
        b2 = x_axel2 - solution[0]
    
    return Equation_group([f"{a1}x {b1}y = {c1}", f"{a2}x {b2}y = {c2}"])
    
    

if __name__ == "__main__":
    eq = get_equation_pair_xy_method()
    aq = get_equation_pair_xy_method_scrambeld()
    wq = get_smart_scramble_equation_for_sub()
    rq = get_good_sub_equation()
    print(str(eq.get_latex()).replace("'", "").replace("[", "").replace("]", ""))
    print(str(aq.get_latex()).replace("'", "").replace("[", "").replace("]", ""))
    print(str(wq.get_latex()).replace("'", "").replace("[", "").replace("]", ""))
    print(str(rq.get_latex()).replace("'", "").replace("[", "").replace("]", ""))