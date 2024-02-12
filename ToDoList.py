#1 This is a small project that allows users to enter, 
# save and edit various activities.

#I create an empty list to be filled with the activities that the user wants to add.

ToDoList = []

#I create a function that allows the user to add the activities he/she wishes to include in the list

def addingActivities(*args):
    for activity in args:
        NewAdded = activity.capitalize().strip()
        ToDoList.append(NewAdded)
        print(f"You added the activity {activity} successfully")


# function to display the complete list of activities

def activitiesVisualizing():
    if not ToDoList:
        print("There aren't activities to be displayed")

    else:
        print("Here you can find the activities you saved:")
        for i, activity in enumerate(ToDoList, start=1):
            print(f"{i} -- {activity}")

# function to allow the user to edit an activity in the list
def editActivity():
    activitiesVisualizing()
    if not ToDoList:
        print("No activity to be displayed")
        return
    try:
        index =int(input("Insert the index of the activity you want to edit "))
        if 1 <= index <= len(ToDoList):
            activityToEdit = input("Insert the new activity you want to insert ")
            ToDoList[index - 1] = activityToEdit
        else:
            print("Indice non valido")
    except ValueError:
        print("Insert a valid index.")

# I create a function to allow the user to delete an activity in the list
def deleteActivity():
    activitiesVisualizing()
    if not ToDoList:
        print("No activity to be displayed")
        return
    try:
        index =int(input("Insert the index of the activity you want to delete "))
        if 1 <= index <= len(ToDoList):
            deletedActivity = ToDoList.pop(index - 1)
            print(f"The activity {deletedActivity} has been deleted")
        else:
            print("No valid Index")
    except ValueError:
        print("Insert a valid Index please")


# Main function for setting user interaction 

def main():
    while True:
        print("\nMenu:")
        print("1. Add activity")
        print("2. Display activities")
        print("3. Edit activities")
        print("4. Delete activities")
        print("5. Exit the application")

        choice = input("Select an option: ")

        if choice == "1":
            #Ask the user to insert an activity
            newActivity = input("Please insert an activity: ")
            manyActivities = newActivity.split(', ')
            addingActivities(*manyActivities)
            print(f"You insert the following activity --> {newActivity}")
        elif choice == "2":
            # diplay all the activities in the list
            activitiesVisualizing()
        elif choice == "3":
            # edit the activity in the list
            editActivity()
        elif choice == "4":
            # delete the activity in the list
            deleteActivity()
        elif choice == "5":
            # Exit the application
            print("Bye and thank you for having used our application!")
            break
        else:
            print("You choose the wrong option. Try again please")

# Run tha main function

if __name__ == "__main__":
    main()