from lxml.html import fragments_fromstring


def to_do_list():
    try:
        task_list =[]
        while True:
            print("Welcome to the to do list app!")
            print("1.Add a new task")
            print("2.View a task")
            print("3.Delete a task")
            print("4.Exit")
            select = int(input("Enter the task you wanted to perform : "))
            if select == 1:
                user = int(input("how many tassk do you want to add : "))
                while user > 0:
                    user_input = input("add new task : ")
                    task_list.append(user_input)
                    user-=1

            elif select ==2 :
                if task_list:
                    for i,task in enumerate(task_list):
                        print(i,task)
                else :
                    print("no tasks")
            elif select == 3:
                print(task_list)
                also = int(input("Enter no of task you want to delete : "))
                for num in range(also):
                    ask = int(input("Enter the index of the task you want to delete: "))
                    task_list.pop(ask)
                print(task_list)
            elif select == 4:
                break
    except ValueError:
        print("enter correct value")

to_do_list()