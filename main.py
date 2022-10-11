speedometer = 1935
speed = 58.3

print (speedometer)
print (speed)

del speedometer
del speed


var1 = var2 = var3 = "salut"
print (var1)
#del var2 # "del" deletes the object
print (var2); print(var3 + " lume")


a, b, c = 4.241, 7, "salut lume"
print (a)
print (b)
print (c)


str1 = "Ready to work?"
print (str1)
print(str1[1])
print(str1[2:8])
print(str1[1:100])
print((str1 + "\n") * 5)


#the following are lists, are enclosed in brackets [], and
#their elements and size can be changed
firstList = [1, 3, "salut", 3.521, ["neata", "lume", 5]]
print (firstList)
print(firstList[4])


str2 = "Wonderfull weather"
#list is a constructor that takes as paramer one argument
#it transforms a string, or dictionary, etc into a list
print(list(str2))




#the following are tuples, are enclosed in parantheses () 
#and their values and size can't be changed. They can be thought of as
#read-only lists. Tuples can be manipulatd like lists(see above)
firstTuple = (1, 2, "a", 3.32)
print(firstTuple)


#the following are dictionaries and are created using curly braces {}.
#The elements can be accessed using [].
firstDictionary = {1:"hello", 2:"world", 3:"!"}
print(firstDictionary)
print(firstDictionary.keys())
print(firstDictionary.values())

