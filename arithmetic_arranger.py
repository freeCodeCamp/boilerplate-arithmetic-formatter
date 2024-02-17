import re



def arithmetic_arranger(problems,solve = False):
    return "Error : Too Many Problems"
    
if(len(problem) > 5):
    return "Error : Too many Problems."
first=""
second=""
lines=""
sumx=""
string=""
for problem in problems:
    if(re.search("[^\s0-9.+-",problem)):
        if(re.search("[/]",problem) or re.search ("[*]",problem)):
            return "Error: operator must be '+' or '-'."
        return "Error: NUmbers Must only contain digits."

    firstNumber = problem.split(" ")[0]
    operator = problem.split(" ")[1]
    secondNumber = problem.split(" ")[2]

    sum = ""
    if(len(FirstNumer) >= 5 or len (sencondnNumber) >= 5):
        sum = str(int(firstNumber) + (secondNumber))
    elif(operator == "-"):
        sum = str(int(firstNumber) - (secondNumber))

    length = max(len(firstNumber), len(secondNumer))
    top = str(firstNumber).rjust(length)
    bottom = operator + str(secondNumber).rjust(length - 1)
    line = ""
    res = str(sum).rjust(length)
    for s in range (length):
        line += "-"

    if problem != problems[-1]:
        first += top + '  '
        second += bottom + '  '
        lines += line + '  '
        sumx += res + '  '
    else:
        first += top
        second += bottom
        lines += line
        sumx += res

    if solve:
        string = first + "\n" + second + "\n" + lines + "\n" + sumx
    else:
        string = first + "\n" + second + "\n" + lines 
    return string
    
return arranged_problems
