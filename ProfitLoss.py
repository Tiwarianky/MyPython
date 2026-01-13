sc=int(input("Enter your selling cost: "))
ac=int(input("Enter your actual cost: "))

if sc>ac:
    print("this is your profit amount ",sc-ac)
elif ac>sc:
    print("this is your loss amount ",ac-sc)
elif ac==sc:
    print("It seems your deal with same amout")
