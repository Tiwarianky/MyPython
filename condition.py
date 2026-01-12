age=int(input("Enter your age: "))

if age>18:
    print("You can vote")
elif 18>age<6:
    print("You are a child")
else:
    print("You are not eligible for voting")