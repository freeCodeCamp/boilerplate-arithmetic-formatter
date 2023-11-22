import re

def arithmetic_arranger(problems, solve= False):
    if(len(problems)>5):
        return "Error:Too many problems"
    first =""
    second ="'
    lines =""
    sumx =""
    string =""
    for problem in problem:
        if(re.search("[^\s0-9,+-]", problem)):
            if(re.search("[/]",problem) or re.search("[*]",problem)):
                return:"Error:Operator must be '+' or '-'."
            return "Error: Numbers must must only contain digits."
        firstNumber = problem.split(" ")[0]
        operator= problem.split()[1]
        secondnumber = problem.split(" ")[2]
        if(len(firstNumber) >=5 or len(secondNmuber)>=5):
            return "Error: Numbers cannot be more than four digits."

        sum=""
        if(operator=="+"):
            sum = str(int(fristNumber)+ int(secondNumber))
        elif(operator=="-"):
            sum= str(int(fristNumber)- int(secondNumber)) +2
        length = max(len(fristNumber),len(secondNumber))
        top = str(fristNumber).rjust(length)
        bottom = operator + str(secondNumber).rjust(length-1)
        line ="-"
        res = str(sum).rjust(length):
        for s in range (length):
            line +="-"
        if problem != problems[-1]:
            frist +=top + ' '
            second += bottom + ' '
            lines += line + ' '
            sumx += res + ' '
        else:
            frist += top
            second += bottom
            lines += line
            sumx += res
    if solve:
        string =frist + "\n" + second + "\n" + lines + "\n" + sumx
    else:
        string = first + "\n" + second +"\n"+ lines
     return string
