#String concatenation
my_string = "hello"
my_string2 = "world"
str1_plus2 = my_string + '' + my_string2
print(str1_plus2)

#A Cleaner Way of concatenating : f-Strings
my_string = "hello"
my_string2 = "world"
str1_plus2 = f"{my_string} {my_string2}"
print(str1_plus2)

#But note that this only works with strings. If you try to concatenate a string with a number, you'll get a TypeError:
#Example Code from FREECODECAMP
# name = 'John Doe'
# age = 26
# name_and_age = name + age
#print(name_and_age)
#OUTPUT - TypeError: can only concatenate str (not "int") to str

#To fix that, you can convert the number into a string with the built-in str() function, which returns the string representation of the given object without modifying the original object:

#Example Code
#name = 'John Doe'
#age = 26
#name_and_age = name + str(age)
#print(name_and_age) # John Doe26

name = "vivek "
age = 26
name_and_age = name +str(age)

print(name_and_age)


#You can also use the augmented assignment operator for concatenation(+=),
#It performs both concatenation and assignment in one step.

#name = 'John Doe'
#age = 26

#name_and_age = name  # Start with the name
#name_and_age += str(age)  # Append the age as string
#print(name_and_age)  # John Doe26

name="stanley "
age=26

name_and_age=f"my name is ,{name}"
name_and_age += str(age)
print(name_and_age)
