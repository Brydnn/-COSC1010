#
# Name Brydnn Killpack 
# Date 9/15/2024
# Hot Dog Cookout Calculator Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

# Constants
hotDogsPerPackage = 10
bunsPerPackage = 8

# Local variables
numberOfPeople = 0      
hotDogsPerPerson = 0   
total_hot_dogs = 0      
minDogs = 0             
minBuns = 0            
dogsLeft = 0            
bunsLeft = 0          

# The number of people who will attend.
numberOfPeople = int(input('Enter the number of people attending the cookout: '))

# number of hot dogs per person
hotDogsPerPerson = int(input('Enter the number of hot dogs per person: '))

# The total of hot dogs
total_hot_dogs = numberOfPeople * hotDogsPerPerson

# The total of hot dog packs
minDogs = total_hot_dogs // hotDogsPerPackage

# The total of bun packs
minBuns = total_hot_dogs // bunsPerPackage

# Determin if you have enough
if minDogs > 0: 
    # Calculate the number of hot dogs left over from a package, if any.
    dogsLeft = total_hot_dogs % hotDogsPerPackage

    # If there will be left overs, add an additional package of hot dogs.
    if dogsLeft != 0:
        minDogs += 1
# Determin if you need to get more
else:
    minDogs =  1

# Determine the number of leftover hot dogs, if any.
dogsLeft = (hotDogsPerPackage * minDogs) - total_hot_dogs

# Determine if the number of people attending will be enough for a pack
if minBuns > 0:
    # Calculate the number of hot dog buns left over from a package, if any.
    bunsLeft = total_hot_dogs % bunsPerPackage

    # If there will be left overs, add an additional package of hot dog buns.
    if bunsLeft != 0:
        minBuns += 1
# The minimum of what you will need 
else:
    minBuns = 1

# Figure out if there is left overs
bunsLeft = (bunsPerPackage * minBuns) - total_hot_dogs

# The minum of pack you will need 
print('Minimum packages of hot dogs needed: ', minDogs)

# The minmum of buns you will need 
print('Minimum packages of hot dog buns needed: ', minBuns)

# The left over of hot dogs
print('Hot dogs left over: ', dogsLeft)

# The left overs of buns
print('Hot dog buns left over: ', bunsLeft)