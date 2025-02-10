from art import logo
#Add
def add(n1, n2):
  return n1 + n2

#Substract
def sub(n1, n2):
  return n1 - n2

#Multiply
def mul(n1, n2):
  return n1 * n2

#Divide
def div(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : sub,
  "*" : mul,
  "/" : div
}
def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  for symbols in operations:
    print(symbols)
  operation_symbol = input("Pick an operation from the line above: ")
  num2 = float(input("What's the second number?: "))
    
  result = operations[operation_symbol](num1, num2)
    
  print(f"{num1} {operation_symbol} {num2} = {result}")
  
  calculating = True
  while calculating:
    choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
    if choice == 'y':
      for symbols in operations:
        print(symbols)
      operation_symbol = input("Pick an operation from the line above: ")
      num = float(input("What's the next number?: "))
      old_result = result
      result = operations[operation_symbol](old_result, num)
      print(f"{old_result} {operation_symbol} {num} = {result}")
    else: 
      calculator()

calculator()
