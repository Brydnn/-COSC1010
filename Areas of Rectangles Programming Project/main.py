#
# Name Brydnn Killpack
# Date 9/15/2024
# Areas of Rectangles Programming Project
# COSC 2409 DNT
#
# Get length A
lengthA=float(input('What is the length of first rectangle? '))
# Get width A
widthA=float(input('What is the width of the first rectangle? '))
# Get length B
lengthB=float(input('What is the length of the second rectangle? '))
# Get width B
widthB=float(input('What is the width of the second rectangle? '))
# Calculate area A
areaA=lengthA*widthA
# Calculate area B
areaB=lengthB*widthB
# Print area comparison using if-elif-else statements
if areaA==areaB:
    print('The area of both rectangles is the same')
    print('Both areas are:' , areaA)
else:
    print('Area of rectangle A equals' , areaA)
    print('Area of rectangle B equals' , areaB)
    if areaA>=areaB:
        print('The area of rectangle A is bigger than rectangle B by' , areaA-areaB)
    else:
        print('The area of rectangle B is greater than rectangle A by' , areaB-areaA)