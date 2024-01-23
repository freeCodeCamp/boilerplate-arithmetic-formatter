



def arithmetic_arranger(problems):
    arranged_problems = {"top": [], "bottom": [], "line": [], "result": []}

    for problem in problems:
        op1, operator, op2 = problem.split()

        width = max(len(op1), len(op2)) + 2
        arranged_problems["top"].append(op1.rjust(width))
        arranged_problems["bottom"].append(operator + op2.rjust(width - 1))
        arranged_problems["line"].append("-" * width)

    return "\n".join([*arranged_problems["top"], *arranged_problems["bottom"], *arranged_problems["line"]])

# Example usage:
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
result = arithmetic_arranger(problems)
print(result)
