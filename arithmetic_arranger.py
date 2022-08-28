def arithmetic_arranger(problems):
    args = []

    len_problems = len(problems)
    if len_problems > 5:
        print("Error: Too many problems.")
        return

    for problem in problems:
        args = problem.split()
        if args[1] in ["%", "*"]:
            print("Error: Operator must be '+' or '-'.")
            return
        if not args[0].isdigit() and args[2].isdigit():
            print("Error: Numbers must only contain digits.")
            return
        if len(args[0]) > 4 or len(args[2]) > 4:
            print("Error: Numbers cannot be more than four digits.")
            return

            # return arranged_problems

    for problem in problems:
        args = problem.split()
        longest = len(max(args[0], args[2], key=len))

        # if len(args[0]) <= len(args[2]):
        #     print(f"{args[0]:>{longest + 2}s}")
        #     print(f"{args[1]} {args[2]}")
        # else:
        print(f"{args[0]:>2}")
        # print(f"{args[1]}{args[2]:>{longest + 2}s}")


if __name__ == '__main__':
    # arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
    arithmetic_arranger(["132 + 68"])
