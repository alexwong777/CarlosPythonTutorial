import easygui

# Create a list of field names
field_names = ["Name", "Age"]

# Create a list of default field values
field_values = ["", ""]

# Display a dialog box with input fields
field_values = easygui.multenterbox("Please enter your information:", "Information", field_names, field_values)

# Check if the user clicked "Cancel" or closed the window
if field_values == None:
    easygui.msgbox("You clicked Cancel or closed the window.", "Information")
else:
    # Extract the values from the list and display them
    name = field_values[0]
    age = field_values[1]

    # Create a list of gender options
    genders = ["Male", "Female", "Other"]

    # Display a button box to select the gender
    gender = easygui.buttonbox("Please select your gender:", "Gender", choices=genders)

    # Display the user's information
    msg = "Your name is " + name + ", you are " + age + " years old, and you identify as " + gender + "."
    easygui.msgbox(msg, "Information")
