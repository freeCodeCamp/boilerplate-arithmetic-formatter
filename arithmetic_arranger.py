import re
import operator

def arithmetic_arranger(problems, solve = False):

    if len(problems) > 5:
        return "Error: too many problems" # checking if the minimum number of problems not exceeded
    
    # innitialize an empty list with a variable arranged_problems

    arranged_problems = []

    for problem in problems: # a loop for checking each problem in problems if the characters are valid
        if re.match(r"[^\s0-9.+-]", problem):
            if re.search(r"[/]", problem) or re.search(r"[*]", problem):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."
        
        # Convert the first and second numbers to integers.
        first_number = int(problem.split(" ")[0])
        second_number = int(problem.split(" ")[2])

        # Chec the letter's length
        if len(str(first_number)) >= 5 or len(str(second_number)) >= 5:
            return "Error: Number can not be more than four digits"
        
        # Performing the arithmetic function

        sum = ""
        if operator == '+':
            sum = str(first_number + second_number)
        
        elif operator == '-':
            sum = str(first_number - second_number)

        # Formating the output string
        length = max(len(str(first_number)), len(str(second_number)))
        arranged_problems.append(f"{first_number:>{length}} {operator} {second_number:>{length-1}}")
        arranged_problems.append(f"{'-'*length:>{length}}")

        if solve:
            arranged_problems.append(f"{sum:>{length}}")
        
    # Remove any whitespace landed from the output
    arranged_problems = [string.lstrip() for string in arranged_problems]

    # Join the output lines into a string.
    arranged_problems_string = "\n".join(arranged_problems)

    return arranged_problems_string
