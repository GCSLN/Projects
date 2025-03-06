import random
random_number = random.randint(1,100)
#print(random_number)
try:
    while True:
        user_value = int(input("Enter the input : "))
        if user_value == random_number:
            print("Successfully guessed")
            break
        else:
            check = random_number - user_value
            if abs(check) < 5:
                print("too close")
            elif abs(check) > 5 and abs(check) < 30:
                print("close")
            elif abs(check) > 30 and abs(check) < 60:
                print("far")
            elif abs(check) > 60 and abs(check) <100:
                print("Too far")
            print("tryagain")

except ValueError:
    print("Enter Only Integer")
except ZeroDivisionError:
    print("Dont Enter Zero")