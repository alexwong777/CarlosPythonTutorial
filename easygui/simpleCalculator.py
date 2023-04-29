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
    # Display a message box to get the user's input
    msg = "Enter two numbers and an operator"
    title = "Calculator"
    fieldNames = ["Number 1", "Number 2", "Operator"]
    fieldValues = easygui.multenterbox(msg, title, fieldNames)

    # Convert the input to numeric values
    try:
        num1 = float(fieldValues[0])
        num2 = float(fieldValues[1])
    except ValueError:
        easygui.msgbox("Please enter valid numbers")
        continue

    # Perform the calculation
    operator = fieldValues[2]
    result = calculate(num1, num2, operator)

    # Display the result
    msg = "The result is: " + str(result)
    title = "Calculator"
    easygui.msgbox(msg, title)

    # Ask the user if they want to continue
    msg = "Do you want to perform another calculation?"
    title = "Calculator"
    if not easygui.ccbox(msg, title):
        break
