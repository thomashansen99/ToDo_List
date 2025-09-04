
def add_todo(item):
    with open("ToDo_List.txt", "a") as file:
        file.write(f"{item}\n")
    
    #full_list.update({f"({count})": item})

def mark_complete(item_num, full_list, count):
    item = full_list.pop(f"{item_num} -")
    with open("Completed_ToDos.txt", "a") as file:
        file.write(f"{item}\n")
    dict_to_file("ToDo_List.txt", full_list)

def delete_todo(item_num, full_list, count):
    item = full_list.pop(f"{item_num} -")
    dict_to_file("ToDo_List.txt", full_list)


def show_all(full_list):
    show = ""
    for key, value in full_list.items():
        show += f"\t{key} {value}\n"
    return show

def file_to_dict(file):
    full_list = {}
    with open(file, "r") as file:
        count = 1
        for line in file:
            line = line.strip()
            if line:
                full_list[f"{count} -"] = line.strip()
                #full_list.update({f"({i})": line.strip()})
                count += 1
    return full_list, count

def dict_to_file(file, full_list):
    with open(file, "w") as file:
        for key, value in full_list.items():
            if value.strip():
                file.write(value + "\n")
    

def main():
    
    #add_todo(input("Type your new to-do here: "), full_list, i)
    #print(show_all(full_list))

    while True:
        print("\nWelcome to the super awesome To-Do List. Here are the menu options:")
        print("(1) Display the To-Do List")
        print("(2) Add something to the list")
        print("(3) Mark something as complete")
        print("(4) Delete something from the list")
        print("(5) Exit the program")
        choice = input("Enter a number from the menu: ")

        if choice == "1": #Display the To-Do List
            print("To-Do List:")
            full_list, count = file_to_dict("ToDo_List.txt")
            print(show_all(full_list))
        elif choice == "2": #Add something to the list
            full_list, count = file_to_dict("ToDo_List.txt")
            add_todo(input("Type your new to-do here: "))
            full_list, count = file_to_dict("ToDo_List.txt")
            print("Here is the updated list: ")
            print(show_all(full_list))
        elif choice == "3": #Mark something as complete
            full_list, count = file_to_dict("ToDo_List.txt")
            print("Here is the current list: ")
            print(show_all(full_list))
            mark_complete(input("Enter the number of the item to mark it as complete: "), full_list, count)
            full_list, count = file_to_dict("ToDo_List.txt")
            print("That item was added to the completed list.\nHere is the updated list: ")
            print(show_all(full_list))
        elif choice == "4": #Delete something from the list
            full_list, count = file_to_dict("ToDo_List.txt")
            print("Here is the current list: ")
            print(show_all(full_list))
            delete_todo(input("Enter the number of the item to delete it: "), full_list, count)
            full_list, count = file_to_dict("ToDo_List.txt")
            print("That item was deleted.\nHere is the updated list: ")
            print(show_all(full_list))

        elif choice == "5": #Exit the program
            print("Goodbye!\n")
            break
        else:
            print("🚫Invalid input. Try again")


if __name__ == "__main__":
    main()