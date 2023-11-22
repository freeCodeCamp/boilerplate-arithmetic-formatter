def arithmetic_arranger(problems, show_answers=False):  # defining a function
  if len(problems) > 5:
    return "Error: Too many problems"  # error message as per rule 1

  errors = []  # Collect errors in a list

  for problem in problems:
    operand1, operator, operand2 = problem.split()

    if operator not in ['+', '-']:
      errors.append(
          "Error: Operator must be '+' or '-'")  #error message a/pr rule2

    if not operand1.isdigit() or not operand2.isdigit():
      errors.append(
          "Error: Numbers must only contain digits")  #error message a/pr
      #rule3

    if len(operand1) > 4 or len(operand2) > 4:
      errors.append("Error: Numbers cannot be more than four digits")
    #error message as/pr rule4

  if errors:
    return "\n".join(errors)  # Returning  all errors

  result_lines = [""] * 3  # defining 3 lines for display

  for problem in problems:
    operand1, operator, operand2 = problem.split()
    width = max(len(operand1), len(operand2)) + 3
    result_lines[0] += operand1.rjust(width) + '    '
    result_lines[1] += operator + ' ' + operand2.rjust(width - 2) + '    '
    result_lines[2] += '-' * width + '    '

    if show_answers:
      answer = str(eval(problem))
      result_lines.append(answer.rjust(width) + '    ')

  result = "\n".join(result_lines).rstrip()
  return result


# Input from the user
num_problems = int(
    input("How many arithmetic problems do you want to solve? "))
user_problems = []

for i in range(num_problems):
  user_problem = input(f"Enter problem {i + 1}: ")
  user_problems.append(user_problem)

# Call the function and display the result
result = arithmetic_arranger(user_problems)
if result.startswith("Error"):
  print(result)  # Display the error message
else:
  print(result)  # Display the arranged arithmetic problems
  # Do something with the correct result
