to_Do_List= []
priority=[]
def view():
    if to_Do_List == "":
       empty() #message appears if user tries to view an empty list
    else:
        for index, item in enumerate(to_Do_List):       #enumerate means  how many items are in the array
            print(f"{index + 1})  {prio_Conversion(index)} {item} \n")

def prio_Conversion(i):
    if priority[i] == "1":
        return "Higb priority"
    elif priority[i] == "2":
        return "Medium priority"
    else:
        return "Low priority"

def add():
    new_Item = input("What do you want to add to the list? \n")
    to_Do_List.append(new_Item)# add item to the array
    new_Prio = input("\n please select the new level of priority \n 1) High priority \n 2) Med priority \n 3) Low priority") 
    if int(new_Prio) > 3 or int(new_Prio) < 1:
        print("error")
    else:
        to_Do_List.append(new_Item)# add item to the array
        priority.append(new_Prio)
    print("\n item added successfully \n \n")

def delete():
    if len(to_Do_List) == 0:
        empty()   #message appears if you try to delete somthing from the list while its empty
    else:
        print(f"what item do you want to delete? {len(to_Do_List)} items in total")
        view()

        del_Choice=input("selection: \n")   #user selects what file they want deleted
        
        if (int(del_Choice)-1) <= (len(to_Do_List) ):  #ensures the user selected a number that actually has a file stored
            to_Do_List.pop(int(del_Choice)-1)
            print("\n item succefully deleted! \n")
        else:
            print("please select an item in the list.")
            #

def save_List(s_list, filename = "py_todo_list.txt"):
    with open(filename, "w") as file:               #open the file in write mode
        for item in s_list:                         # write each item in the array line by line
            file.write(item + "\n") 
        save_Prio(priority)
        print("File saved succesfully")

def save_Prio(p_list, filename = "py_prio_list.txt"):
    with open(filename, "w") as file:               #open the file in write mode
        for item in p_list:                         # write each item in the array line by line
            file.write(item + "\n") 
        print("Priority saved succesfully")

def empty():
    print("sorry! your to do list is empty.")   #message appears if you try to interact with the list while its empty

def priority_Change():
    if to_Do_List =="":
        empty()
    else:
        view()
        prio_choice = input("what item's priority do you want to change? \n")
        if (int(prio_choice) - 1) <= (len(to_Do_List)):
            view()
            try:
                prio_Rank=input("\n please select the new level of priority \n 1) High priority \n 2) Med priority \n 3) Low priority")
                priority[int(prio_choice)-1] = prio_Rank
            except:
                print("please enter a valid priority ranking")







    


           






with open("py_todo_list.txt", "r") as file:                  #opens the list upon startup
    to_Do_List = [line.strip() for line in file.readlines()]
with open("py_prio_list.txt", "r") as file:                  #opens the list upon startup
    priority = [line.strip() for line in file.readlines()]


while True:       
        menu=input("Welcome to the to do list! \n 1) view your tasks, \n 2) add new task \n 3) delete a task \n 4) save list \n 5) exit \n" )        # the main menu, allows user to navigate their different options
        if menu == "1":
            view()
        elif menu == "2":
           add()
        elif menu == "3":
            delete()
        elif menu == "4":
            save_List(to_Do_List)
        elif menu == "5":
            break
        else:
            print("sorry pick a valid value")     #message appears if the user types an invalid input