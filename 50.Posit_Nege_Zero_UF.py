a = int(input("Enter a Integer : "))
def positive():
    print(f"Entered Integer is Positive.")
def negative():
    print("Entered Integer is Negative.")
def zero():
    print("Enterd Integer is Zero")
if a == 0 :
    zero()
elif a < 0:
    negative()
else:
    positive()
