import sys
type(sys.path)
sys.path.append(r"C:\Users\Leevi Suotula\AppData\Local\Own python\funktio_moniste\objects")
sys.path.append(r"c:\users\leevi suotula\anaconda3\lib\site-packages")
from random import randint


from objects import equation_pair_randomiser
ids = []
for i in range(30):
    id = randint(1000, 9999)
    while id in ids:
        id = randint(1000, 9999)
    ids.append(id)
    mdfolder = r"C:\Users\Leevi Suotula\AppData\Local\Own python\funktio_moniste\final pdfs\raw\\"
    efolder = r"C:\Users\Leevi Suotula\AppData\Local\Own python\funktio_moniste\final pdfs\Exercises\\"
    sfolder = r"C:\Users\Leevi Suotula\AppData\Local\Own python\funktio_moniste\final pdfs\Solutions\\"
    hfolder = r"C:\Users\Leevi Suotula\AppData\Local\Own python\funktio_moniste\final pdfs\html_files\\"
    exercise_md_filename = mdfolder + f"{id} Funktiopari.md"
    solution_md_filename = mdfolder + f"{id} Funktiopari ratkaisut.md"
    exercise_pdf_filename = efolder + f"{id} Funktiopari.pdf"
    solution_pdf_filename = sfolder + f"{id} Funktiopari ratkaisut.pdf"
    exercise_html_filename = hfolder + f"{id} Funktiopari.html"
    solution_html_filename =  hfolder + f"{id} Funktiopari ratkaisut.html"
    
    with open(exercise_md_filename, "w") as f:
        solutions = []
        f.write('<style type="text/css">\n')
        f.write('\tol { list-style-type: upper-alpha; }\n')
        f.write('</style>')
        f.write("\n\n")
        f.write("### 9 lk funktiopari moniste\n")
        f.write(f"id = {id}\n")
        
        def write_function_group(function_group, file):
            eq = function_group.get_latex()
            file.write("\n")
            file.write("$$\n")
            file.write("\left\{\n")
            file.write("\t"+r"\begin{aligned}"+"\n")
            center_part = "\t\t"
            for i in range(len(eq)):
                function = eq[i]
                center_part += function
                if i != len(function) - 1:
                    center_part += "\\\\"
            center_part += "\n"
            file.write(center_part)
            file.write("\t"+r"\end{aligned}"+"\n")
            file.write(r"\right."+"\n")
            file.write("$$\n")
            
        def write_exercise_function_pair_1(num, file, difficulty, randomrange = 7):
            file.write(f"#### {num}. Raktaise yhtälöparit\n")
            solutions.append([])
            for i in range(4):
                file.write(str(i+1)+".")
                eq = equation_pair_randomiser.get_equation(randomrange, difficulty)
                solutions[num-1].append(eq[1])
                write_function_group(eq[0], f)


        write_exercise_function_pair_1(1, f, -1, 5)
        write_exercise_function_pair_1(2, f, -1)
        write_exercise_function_pair_1(3, f, 0, 5)
        write_exercise_function_pair_1(4, f, 0)
        write_exercise_function_pair_1(5, f, 1, 5)
        write_exercise_function_pair_1(6, f, 1)
        write_exercise_function_pair_1(7, f, 1, 9)
        write_exercise_function_pair_1(8, f, 2, 5)
        write_exercise_function_pair_1(9, f, 2)
        write_exercise_function_pair_1(10, f, 2, 9)
    
    with open(solution_md_filename, "w") as f:
        f.write('<style type="text/css">\n')
        f.write('\tol { list-style-type: upper-alpha; }\n')
        f.write('</style>')
        f.write("\n\n")
        f.write("### Ratkaisut\n")
        f.write(f"id = {id} \n\n")
        for i in range(len(solutions)):
            f.write(f"Tehtävä {i+1} \n\n")
            for j in range(len(solutions[i])):
                f.write(str(j+1)+".")
                f.write("\n")
                f.write("$$\n")
                f.write("\left\{\n")
                f.write("\t"+r"\begin{aligned}"+"\n")
                center_part = f"\t\tx={solutions[i][j][0]}\\\\y={solutions[i][j][1]}\n"
                f.write(center_part)
                f.write("\t"+r"\end{aligned}"+"\n")
                f.write(r"\right."+"\n")
                f.write("$$\n")
    

        def mrkdw_to_pdf(start, middle, goal):
            with open(start, 'r') as f:
                tempMD = f.read()
            tempHtml = markdown2.markdown(tempMD)
            with open(middle, 'w') as f:
                f.write(tempHtml)