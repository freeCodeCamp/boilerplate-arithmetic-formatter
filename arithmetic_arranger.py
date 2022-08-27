def arithmetic_arranger(problems):
    print(problems)
    maList=[]
    for problem in problems:
        args = problem.split()
        maList.append(args)
        print(maList)
        tab = abs(len(args[0]) - len(args[1]))
        maxLen = len(args[2])

        # if len(args[0]) < len(args[2]):
        #     print(f"{args[0]:>{maxLen + 2}s}\n{args[1]} {args[2]}")

    # return arranged_problems


if __name__ == '__main__':
    # arithmetic_arranger(["32 + 600133338"])
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
    #
