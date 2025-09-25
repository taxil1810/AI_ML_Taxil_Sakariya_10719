print("\n=======Welcome to the pattern and number analyzer!=======\n")

while True:
    print("Select an option \n")
    print("1.Genrate a pattern")
    print("2.Analyze a numbers")
    print("3.Exit")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        row = int(input("Enter the number of row for the pattern:"))

        print("pattern: ")

        for i in range(1 , row + 1):
                print("*" * i)
                
    elif choice == 2:

        start = int(input("Enter start of the range:"))
        end = int(input("Enter the end of the number:"))
        total = 0

        for i in range (start , end + 1):
            if i % 2 == 0:
                print("number", i , "is even")
            else:
                print("number" , i , "is odd")
            total = total + i
        print("sum of all numbers form" , start ,"to" , end , "is:" , total)

    elif choice == 3:
        print("\n======exiting the program. Good Buy ======")
        break




