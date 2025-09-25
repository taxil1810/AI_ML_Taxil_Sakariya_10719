print("\n ====== Welcome to the Interactive Personal Data Collector ====== \n")

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
height = float(input("Please enter your height in meters: "))
fav_number = int(input("Please enter your favourite number: "))

print("\n ====== Thank you! Here is the information we collected ====== \n")

print("Name:" , name , "type:" , type(name) , "Memory Address:" , id(name))
print("Age:" , age , "type:" , type(age) , "Memory Address:" , id(age))
print("Height:" , height , "type:" , type(height) , "Memory Address:" , id(height))
print("Favourite Number:" , fav_number , "type:" , type(fav_number) , "Memory Address:" , id(fav_number))

birth_year = 2025 - age
print("Your birth year is approximately:" , birth_year)

print("\n ====== Thank you! for using the Personal Data Collector. Goodbye ====== \n")