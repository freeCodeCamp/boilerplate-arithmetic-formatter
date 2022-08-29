def arithmetic_arranger(problems, *option):
    tabs = []
    list_args = []
    line_1 = []
    line_2 = []
    line_3 = []

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
        line_1.append(args[0])
        line_2.append(args[1])
        line_3.append(args[2])
        for i in range(3):
            list_args.append(args[i])
        tab = len(max(args[0], args[2], key=len))
        tabs.append(tab)
    for i in range(len(line_1)):
        if len(line_1[i]) <= len(line_3[i]):
            print(f"{line_1[i]:>{tabs[i] + 2}s}", end="    ")
        else:
            print(f"{line_1[i]:>{tabs[i] + 1}s}", end="    ")

    print("\n")
    for i in range(len(line_1)):
        if len(line_1[i]) <= len(line_3[i]):
            print(f"{line_2[i]} {line_3[i]}", end="    ")
        else:
            print(f"{line_2[i]}{line_3[i]:>{tabs[i]}}", end="    ")
    print("\n")
    for i in range(len(line_1)):
        if len(line_1[i]) > len(line_3[i]):
            for p in range(tabs[i] + 1):
                print("-", end="")
            print(end="    ")
        else:
            for p in range(tabs[i] + 2):
                print("-", end="")
            print(end="    ")
    print("\n")
    for i in range(len(line_1)):
        if len(line_1[i]) > len(line_3[i]):
            if option:
                print(f" {int(line_1[i]) + int(line_3[i])}", end="    ")
        else:
            if option:
                print(f"  {int(line_1[i]) + int(line_3[i])}", end="    ")


if __name__ == '__main__':
    arithmetic_arranger(["32 + 698", "301 - 2", "45 + 43", "123 + 49", "254 + 58"], True)
    # arithmetic_arranger(["132 + 1168"], True)
    # arithmetic_arranger(["312 + 68", "101 - 32", "145 + 53", "123 + 49"])
