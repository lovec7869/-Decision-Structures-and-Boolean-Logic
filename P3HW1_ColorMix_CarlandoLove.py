# Design a program to prompt the user to enter two primary colors.
 # CTI-110
 # P3HW1 - Color Mixer
 # Carlando Love
 # June 24, 2020
 #

primaryColor1 = input( "enter primaryColor1: ")
primaryColor2 = input( "enter primaryColor2: ")

# user to enter the names of two primary colors to mix, secondry color should display
# primaryColors are ("red,"blue","yellow")
# if user enters anything other than primary colors 
# the program should display an error message.

if (primaryColor1 == "red" and primaryColor2 == "blue" ) or \
   (primaryColor1 == "blue" and primaryColor2 == "red" ):
    print(primaryColor1 + " mixed with " + primaryColor2 + " is purple" )
elif ( primaryColor1 == "red" and primaryColor2 == "yellow" ) or \
     ( primaryColor1 == "yellow" and primaryColor2 == "red" ):
    print( primaryColor1 + " mixed with " + primaryColor2 + " is orange" )
elif ( primaryColor1 == "blue" and primaryColor2 == "yellow" ) or \
     ( primaryColor1 == "yellow" and primaryColor2 == "blue" ):
    print( primaryColor1 + " mixed with " + primaryColor2 + " is green" )
else:
    print( " has to be two primaryColors, " + primaryColor1 + " and " + primaryColor2 + " is not a primaryColor" )


 

 

