'''
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
    '''
import re
import math

#split işlemindeki indeks sayıları
firstNumIndex = 0
operatorIndex = 1
secondNumIndex = 2

#sayıların maksimum karakter sayısı
maxDigit = 4
#işlemler arası boşluk sayısı
spacePerProblem = 4

def arithmetic_arranger(problems, sol=False):
  count = 1
  #cevaplanıp cevaplanmayacağını kontrol eder
  answer = False

  if sol:
    #problems = problems[0]
    answer = True

  #soruları tek tek saklamak için boş liste tanımı
  splitQuestion = []
  splitQuestion.clear()
  #her işlem için iki sayı arasındaki en fazla karakterli olan sayının basamak sayısını tutan liste
  maxDigitEachProblem = []
  maxDigitEachProblem.clear()
  #sırasıyla işlemleri saklayacak boş liste tanımı
  operators = []
  operators.clear()
  #her satır için boş liste
  section1 = ["  "] # her zaman ilk iki karakter boşluk
  section2 = []     # ilk karakter operatör ile başlayacak
  section3 = ["--"] # her zaman ilk iki karakter "-"
  section4 = []

  #problem sayısı hata kontrolü
  if len(problems) >= 6:
    return "Error: Too many problems."

  for question in problems:
    '''
    split işlemi
    1. split ilk sayı    - splitQuestion [0] - firstNumIndex
    2. split işlem       - splitQuestion [1] - operatorIndex
    3. split ikinci sayı - splitQuestion [2] - secondNumIndex
    '''
    splitQuestion = re.split("\s", question)

    #sayıların sayı olup olmaması kontrolü
    if not splitQuestion[secondNumIndex].isdigit() \
    or not splitQuestion[firstNumIndex].isdigit():
      return "Error: Numbers must only contain digits."

    #dört basamaktan büyük sayı hata kontrolü
    num1 = int(splitQuestion[firstNumIndex])
    num2 = int(splitQuestion[secondNumIndex])
    num1Digit = howManyDigit(num1)
    num2Digit = howManyDigit(num2)
    if num1Digit > maxDigit or num2Digit > maxDigit:
      return "Error: Numbers cannot be more than four digits."

    #sırasıyla her işlem için maksimum basamağa sahip sayının basamağını saklar
    maxDigitEachProblem = max(num1Digit, num2Digit)

    #operatör hata kontrolü
    operator = splitQuestion[operatorIndex]
    #if not splitQuestion[operatorIndex] in ("+","-"):


    if operator == '+':
      solution = num1 + num2
    elif operator == '-':
      solution = num1 - num2
    else:
      return "Error: Operator must be '+' or '-'."
    solutionDigit = howManyDigit(solution)

    section1.append(" " * (maxDigitEachProblem - num1Digit))
    section1.append(str(num1))
    section2.append(operator)
    section2.append(" ")
    section2.append(" " * (maxDigitEachProblem - num2Digit))
    section2.append(str(num2))
    section3.append("-" * maxDigitEachProblem)
    section4.append(" " * ((maxDigitEachProblem + 2) - solutionDigit))
    section4.append(str(solution))

    if count < len(problems):
      section1.append(" " * spacePerProblem)
      section1.append("  ")
      section2.append(" " * spacePerProblem)
      section3.append(" " * spacePerProblem)
      section3.append("--")
      section4.append(" " * spacePerProblem)

    section1Final = "".join(section1)
    section2Final = "".join(section2)
    section3Final = "".join(section3)
    section4Final = "".join(section4)
    count = count + 1

  if answer == True:
    return section1Final + "\n" + section2Final + "\n" + section3Final + "\n" + section4Final
  return section1Final + "\n" + section2Final + "\n" + section3Final

#basamak sayısını döndüren fonksiyon
def howManyDigit(number):
  if number > 0:
    digits = int(math.log10(number))+1
  elif number == 0:
    digits = 1
  elif number < 0:
    digits = int(math.log10(-number))+2
  return digits

    # Join the output lines into a string.
    arranged_problems_string = "\n".join(arranged_problems)

    return arranged_problems_string
