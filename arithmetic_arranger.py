import re

def arithmetic_arranger(problems, solve=False):
  if len(problems) > 5:
    return "Error: Too many problems."
  
  first = ""
  second = ""
  lines = ""
  sumx = ""
  string = ""
  sum = ""
  
  for problem in problems:
    if re.search("[^\s0-9.+-]", problem):
      if re.search("/", problem) or re.search("[*]", problem):
        return "Error: Operator must be '+' or '-'."
      return "Error: Numbers must only contain digits."
      
    num1 = problem.split(" ")[0]
    operator = problem.split(" ")[1]
    num2 = problem.split(" ")[2]
    if len(num1) > 4 or len(num2) > 4:
      return "Error: Numbers cannot be more than four digits."
    if operator == "+":
      sum = str(int(num1) + int(num2))
    elif operator == "-":
      sum = str(int(num1) - int(num2))
      
    lenght = max(len(num1), len(num2)) + 2
    top = str(num1).rjust(lenght)
    bottom = operator + str(num2).rjust(lenght - 1)
    line = ""
    res = str(sum).rjust(lenght)
    
    for s in range(lenght):
      line += "-"
    
    if problem != problems[-1]:
      first += top + "    "
      second += bottom + "    "
      lines += line + "    "
      sumx += res + "    "
    else:
      first += top
      second += bottom
      lines += line
      sumx += res
      
  if solve:
    string = first + "\n" + second + "\n" + lines + "\n" + sumx
  else:
    string = first + "\n" + second + "\n" + lines
  return string