import easygui

# Create a function to perform the calculation
def calculate(num1, num2, operator):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        result = "Invalid operator"
    return result

# Create a loop to keep the calculator running
while True:
    # Create a list of fields for the user to input the numbers and operator
    msg = "Calculator"
    title = "Calculator"
    field_names = ["Number 1", "Operator", "Number 2"]
    field_values = ["", "", ""]
    field_values = easygui.multenterbox(msg, title, field_names, field_values)

    # Check if the user has clicked "Cancel" or closed the window
    if field_values == None:
        break

    # Extract the values from the list and convert them to the appropriate data types
    num1 = float(field_values[0])
    operator = field_values[1]
    num2 = float(field_values[2])

    # Perform the calculation and display the result
    result = calculate(num1, num2, operator)
    msg = "The result is: " + str(result)
    title = "Calculator"
    easygui.msgbox(msg, title)

# End the program
easygui.msgbox("Thanks for using the calculator!", "Calculator")
