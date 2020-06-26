# Rewrite the code to display the use of proper
# conventions, alignment and indentation
# CTI-110
# P3LAB - Debugging
# Carlando Love
# June 27 2020
#

score = int(input("enter your test score: "))
if score >= 90:
    print("your grade is an A")
else:
    if score >= 80:
        print("your grade is a B")
    else:
        if score >= 70:
            print ("your grade is a C")
        else:
            if score >= 60:
                print("your grade is a D")
            else:
                print("your grade is an F")
                
