from logo import logo
def add (num1,num2):
    """return the sum of num1 and num2"""
    return num1+num2
def subtract (num1,num2):
    """return the subtract of num1 and num2"""
    return num1-num2
def multiply (num1,num2):
    """return the multiply of num1 and num2"""
    return num1*num2
def divide (num1,num2):
    """return the divide of num1 and num2"""
    return num1/num2
operators={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
def calculator():    
    print(logo)
    num1=float(input("Type the first number: "))
    finshed_calculating=False
    for operator in operators:
        print(operator)
    while not finshed_calculating:
        choosen_operator=input("Choose operator from the above list: ")
        num2=float(input("Type the next number: "))
        calculate_function=operators[choosen_operator]
        answer=calculate_function(num1,num2)
        print(f"{num1} {choosen_operator} {num2} = {answer}")
        what_next=input("Want to continue with the previous answer? type 'Y', to start new calculation type 'N' or to exit type 'C'").lower()
        if what_next=="y":
            num1=answer
        elif what_next=="n":
            finshed_calculating=True
            calculator()
        elif what_next=="c":
            finshed_calculating=True
calculator()