def arithmetic_arranger(problems):
    maList = []
    tab = []
    for problem in problems:
        args = problem.split()
        for i in range(3):
            if args[i] not in ["+", "-"]:
                maList.append(args[i])

    # connaitre le plus grand des deux valeurs
    print(maList)
    tail = len(maList)
    print(tail)
    comp = [0, 2, 4, 6]
    for i in comp:
        print(maList[i], maList[i + 1])
        tab.append(len(max(maList[i], maList[i + 1], key=len)))

    print(tab)
    for c, t in zip(comp, tab):
        print(f"{maList[c]:>{t + 6}s}", end="")
    print("\n")
    comp2 = [1, 3, 5, 7]
    for c2, t in zip(comp2, tab):
        print(f"{'+':>{tab[t]}s} {maList[c2]}", end="    ")


#     for i in len(maList):
#         if maList[i]<maList[i+2]:
#             tab.append(len(maList[i+2]))

# tab = abs(len(args[0]) - len(args[1]))
# maxLen = len(args[2])

# if len(args[0]) < len(args[2]):
#     print(f"{args[0]:>{maxLen + 2}s}\n{args[1]} {args[2]}")

# return arranged_problems


if __name__ == '__main__':
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
    #
