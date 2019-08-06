print("Hello world")
numbers =["1","2","3","4","5","6"]
print('test')
for number in numbers:
    print(f" Number {number}")

print("\n\nDifferent for statement ")
x=0
for number in numbers:
    print(" Number {0} test".format(number))
    for index in range(10):
        x=x+10
        print("{0}".format(x))

x=0
for index in range(5,50,10):
    x=x+5
    print("{0}".format(x))

print ("Break and Continue")

biggest_num=100

print("Biggest num is greater than 10") if biggest_num>10 else print("Biggest num is not greater than 10 ")
print("Assignment to")
aa="Biggest num is greater than 10" if biggest_num>10 else "Biggest num is not greater than 10"
print(aa)

