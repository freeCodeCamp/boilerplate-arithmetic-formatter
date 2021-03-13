def arithmetic_arranger(problems, check=False):
    operators = []  # -> ['+', '-', '+', '+']
    upper_operand = []  # ->['32', '3801', '45', '123']
    lower_operand = []  # ->['698', '2', '43', '49']
    ops_list = []  # ->[['32', '+', '698'], ['3801', '-', '2'], ['45', '+', '43'], ['123', '+', '49']]

    if len(problems)>5:
        return "Error: Too many problems."



    for item in problems:
        aux_lst = item.split(" ")
        upper_operand.append(aux_lst[0])
        lower_operand.append(aux_lst[2])
        operators.append(aux_lst[1])
        ops_list.append(aux_lst)



        if '*' in operators or '/' in operators:
            return "Error: Operator must be '+' or '-'."

        elif len(aux_lst[0])>4 or len(aux_lst[2])>4:
            return "Error: Numbers cannot be more than four digits."

        elif aux_lst[0].isdigit() ==False or aux_lst[2].isdigit()==False:
            return "Error: Numbers must only contain digits."




    x = printer(upper_operand, lower_operand,operators,ops_list, check)
    print(x)
    return x


def operations(aux_lst):
    if '+' in aux_lst:
        sum = int(aux_lst[0]) + int(aux_lst[2])
        return sum
    else:
        sub = int(aux_lst[0]) - int(aux_lst[2])
        return sub


def printer(upper_operand, lower_operand, operators,ops_list, check=False):
    first_line = ""
    second_line = ""
    third_line = ""
    result_line= ""

    for i in range(len(upper_operand)):

        x = max((len(upper_operand[i]), len(lower_operand[i])))
        upper_shift = x + 2
        lower_shift = x+1


        if i<(len(upper_operand)-1):

            first_line =first_line+f"{upper_operand[i]:>{upper_shift}}"+"    "
            second_line= second_line+f"{operators[i]}{lower_operand[i]:>{lower_shift}}"+"    "
            third_line=third_line+"-"*upper_shift+"    "
            result_line = result_line + f"{operations(ops_list[i]):>{upper_shift}}" + "    "
        else:
            first_line = first_line + f"{upper_operand[i]:>{upper_shift}}"
            second_line = second_line + f"{operators[i]}{lower_operand[i]:>{lower_shift}}"
            third_line = third_line + "-" * upper_shift

            result_line =result_line+f"{operations(ops_list[i]):>{upper_shift}}"
    if check ==True:


        return first_line+"\n"+second_line+"\n"+third_line+"\n"+result_line
    else:

        return first_line+"\n"+second_line+"\n"+third_line






arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
