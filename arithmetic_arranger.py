def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems"

    arranged_problems = []
    for problem in problems:
        operands, operator = map(str.strip, problem.split())

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'"

        if not (operands[0].isdigit() and operands[2].isdigit()):
            return "Error: Numbers must only contain digits"

        if len(operands[0]) > 4 or len(operands[2]) > 4:
            return "Error: Numbers cannot be more than four digits"

        if operator == '+':
            result = int(operands[0]) + int(operands[2])
        else:
            result = int(operands[0]) - int(operands[2])

        max_width = max(len(operands[0]), len(operands[2]))

        arranged_problems.append(
            f"{operands[0].rjust(max_width + 2)}\n"
            f"{operator} {operands[2].rjust(max_width)}\n"
            f"{'-' * (max_width + 2)}\n"
        )

    if show_answers:
        answers = [str(eval(problem)) for problem in problems]
        arranged_problems.append(
            f"{answers[0].rjust(max_width + 2)}\n"
            f"{answers[1].rjust(max_width + 2)}\n"
            f"{answers[2].rjust(max_width + 2)}\n"
            f"{answers[3].rjust(max_width + 2)}\n"
        )

    return '    '.join(arranged_problems[:-1])  # Joining all problems except the last one


# Example usage:
problems_list1 = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
problems_list2 = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]

print(arithmetic_arranger(problems_list1))
print(arithmetic_arranger(problems_list2, True))
