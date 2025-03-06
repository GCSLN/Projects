import math


def operation(Operation, number):
    if Operation == 1:
        return sum(number_list)
    elif Operation == 2:
        result = number_list[0]
        for num in number_list[1:]:
            result -= num
        return result
    elif Operation == 3:
        result = number_list[0]
        for num in number_list[1:]:
            result *= num
        return result
    elif Operation == 4:
        result = number_list[0]
        for num in number_list[1:]:
            result /= num
        return result
    else:
        print("Please Select only the given Calculations")


def single_operation(Operation, num_3):
    if Operation == 5:
        return 'sin of given number', math.sin(num_3)
    elif Operation == 6:
        return 'cos of given number', math.cos(num_3)
    elif Operation == 7:
        return 'tan of given number', math.tan(num_3)
    elif Operation == 8:
        if num_3 < 0:
            return "Negative Number not allowed"
        else:
            return 'sqrt of given number', math.sqrt(num_3)
    elif Operation == 9:
        return 'exp of 2 numbers', num_3 ** num_3
    else:
        return "Please Select only the given Calculations"
print("!This is a Simple Calculator")
print("1.Addition")
print("2.Subtraction")
print("3.division")
print("4.multiplication")
print("5.sin")
print("6.cos")
print("7.tan")
print("8.exponent")
print("9.square root")
try:
    print("Since this is a Simple Calculator we will perform only on 10 samples")
    Operation = int(input("Enter the Required Operation : "))
    if Operation > 9 or Operation < 1:
        raise ValueError()
    elif Operation in [1,2,3,4]:
        i = 10
        number_list = []
        while i >0:
            print("Enter zero to stop and continue operation!!")
            num = int(input("Kindly enter the number : "))
            if num == 0:
                break
            else:
                number_list.append(num)
                print(i-1, "entries left")
                i-=1
        print(operation(Operation,number_list))
    elif Operation in [5,6,7,8,9]:
        num_3 = int(input("Kindly enter the input : "))
        print(single_operation(Operation, num_3))
except ValueError:
    print("Out of Bounds")
except ZeroDivisionError:
    print("please dont enter zero")

        





