from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2
 
def subtract(n1, n2):
    return n1 - n2
 
def multiply(n1, n2):
    return n1 * n2
 
def divide(n1, n2):
    return n1 / n2

math_functions = {}

math_functions["+"] = add 
math_functions["-"] = subtract
math_functions["*"] = multiply
math_functions["/"] = divide

# function = math_functions["+"]
def calculator():
    first_num = float(input("What's the first number? "))
    for key in math_functions:
        print(key)
        
    user_choice = input("Pick an operation from the ones above ")
    second_num = float(input("What's the second number? "))

    function = math_functions[user_choice]
    answer = function(first_num, second_num)
    print(f"{first_num} {user_choice} {second_num} = {answer}")

    redo = input("Would you like to continue with this number? 'Y' or 'N' ")

    if redo == "y":
        while redo == "y":

            print(f"Current number is {answer}")

            for key in math_functions:
                print(key)

            user_choice = input("Pick an operation from the ones above ")
            second_num = float(input("What's the second number? "))

            function = math_functions[user_choice]
            answer = function(answer, second_num)
            print(f"{answer} {user_choice} {second_num} = {answer}")

            redo = input("Would you like to continue with this number? 'Y' or 'N' ")
    start_over = input("Would you like to start over with new numbers? 'Y' or 'N' ")
    if start_over == "y":
        calculator()
calculator()
            
print("Toodles")