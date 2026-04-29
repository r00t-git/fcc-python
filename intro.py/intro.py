my_set={"location","here", "age" , 25,"who","buda"}#Items float around randomly and they don't duplicate values in the output.
print(my_set)


print(type("who"))#shows tha datatype of a value
print(type(25))

my_dictionary={"location":"here", "age":35, "who":"buda"}#Storing data with specific attributes (like a user profile or a product's price).
print(my_dictionary)

my_list=["twenty", 34, "green"] #An ordered, numbered line.The first thing you put in stays at index 0.Duplicates?-If you have five "pigeons," it stores all five.
print(my_list)

#STUDY 2

name=input("what's your name?")
if name=="r00t": #== is the same as 'is'
    print("Access granted! Welcome!")

else:
    print("Not Authorised!")



#STUDY 3

def hello(to="Dear"): #you set a "safety net."
    print("hello,", to)
hello()#When you call hello() without a name, it doesn't crash; it defaults to "Dear."

name = input("what's your name? ").strip().title()#.strip() removes accidental spaces (like if the user hits the spacebar by mistake).
hello(name) #.title() ensures the first letter is capitalized, making your output look polished.

game = input("favourite game? ").title()
print(f"Oh! I like {game} too! ")#this is called an f-string. It’s basically a way to tell Python: "Hey, look inside this string for curly braces {} and replace them with the actual value of a variable."
x = int(input("provide a 2-digit number "))
y = int(input("provide a 3-digit number "))
z = y // x  # / operator always results in a Float (a decimal), even if the numbers divide perfectly (e.g., 100 / 10 results in 10.0).
# If you ever want to get rid of the decimal entirely, you can use // (Integer Division).

print(f"If we divide {y} by {x}, we'll get {z:,}")
#The :, in  {z:,} in tells Python: "If this number is big (like 1,000), put a comma in it." Even though you're doing division, it keeps the output readable.


#List: Use this for a log of events happening in order.

#Dictionary: Use this for device configurations (e.g., {"Interface": "Gigabit0/1", "Status": "Up"}).

#Set: Use this to clean up logs when you only want to see which different types of errors occurred, not how many times they happened.