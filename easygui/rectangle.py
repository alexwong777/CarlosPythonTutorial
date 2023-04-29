import easygui

# Ask the user for the length and width of the rectangle
msg = "Enter the length and width of the rectangle:"
title = "Rectangle Area Calculator"
fields = ["Length:", "Width:"]
values = easygui.multenterbox(msg, title, fields)

# Convert the input to numbers and calculate the area
length = float(values[0])
width = float(values[1])
area = length * width

# Display the area of the rectangle
msg = "The area of the rectangle is " + str(area) + " square units."
title = "Rectangle Area Calculator"
easygui.msgbox(msg, title)
