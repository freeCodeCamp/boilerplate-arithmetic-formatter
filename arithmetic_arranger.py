

def arithmetic_arranger(problems, show_answers=False):
    arranged_problems = {"top": [], "bottom": [], "line": [], "result": []}

    for problem in problems:
        op1, operator, op2 = problem.split()

        width = max(len(op1), len(op2)) + 2
        arranged_problems["top"].append(op1.rjust(width))
        arranged_problems["bottom"].append(operator + op2.rjust(width - 1))
        arranged_problems["line"].append("-" * width)

        if show_answers:
            result = str(eval(problem)).rjust(width)
            arranged_problems["result"].append(result)

    if show_answers:
        return "\n".join([*arranged_problems["top"], *arranged_problems["bottom"], *arranged_problems["line"], *arranged_problems["result"]])
    else:
        return "\n".join([*arranged_problems["top"], *arranged_problems["bottom"], *arranged_problems["line"]])

# Example usage:
problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
result_with_answers = arithmetic_arranger(problems, show_answers=True)
print(result_with_answers)
