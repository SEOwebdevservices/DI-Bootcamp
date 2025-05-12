#loops: for and while Loops
fruits = ["apple", "banana", "Kiwi", "pear"]
for each_fruite in fruits:
    print(f"I love {each_fruite}")

for i in range(1, 11):
    print(i)

#While Loops: condition
num = 0
while num<= 10:
    print(num)
    num+= 1

    num = 1
while num<= 10:
    if num ==5:
        break
    print(num)
    num+= 1

    secret_num = 77
    user_num = int(input("try a number"))

    while user_num != secret_num:
        print("not the number, try again or type q to quit")
        if user_num =="q":
            break
       # else:
            #user_num = int(input("try a number"))
    #else:
       # print("Congrats you win")
