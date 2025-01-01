while True:
    try:
        x = int(input("Enter a number :"))
        break
    except:
        print("something went wrong!")
if x%2 != 0:
    print("odd num!")
else:
    print("even num!")