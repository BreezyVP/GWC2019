#imports the ability to get a random number (we will learn more about this later!)
from random import *
aRandomNumber = randint(0, 3)
#Create the list of words you want to choose from.
aList = ["Summer day", "Sun has set", "Dark grows" ]
bList = ["Cool winds blow west", "Flowers now sleep", "Stars shine bright"]
cList = ["Rainbow sky", "Day is done", "Nightfall"]
#Generates a random integer.
print (aList[aRandomNumber],bList [aRandomNumber], cList[aRandomNumber])
