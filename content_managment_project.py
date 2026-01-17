
import json
# A function to add a person to the contact list 
def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")
    # creating a dictionary to store person details
    person = {"name": name, "age": age, "email": email}
    return person

def display_people(people):
  for i, person in enumerate(people):
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"]) 

# A function to delete a contact from the list
def delete_contact(people):
    # displaying all contacts with index number 
    display_people(people)
    # loop until a valid number is entered
    while True:
        number = input("Enter a number to delete: ")
        try:
            number = int(number) 
            if number <= 0 or number > len(people):
                print("Invalid number, out of range.")
            else:
                break
        except ValueError:
            print("Invalid number")
    people.pop(number - 1)
    print("Person deleted!")
# A function to search for a contact by name
def search(people):
    search_name = input("Search for name: ").lower()
    results = []
    
    for person in people:
        name = person["name"]
        if search_name in name.lower():
            results.append(person)

    display_people(results)

# print greeting message
print("Hello, welcome to the content management system")
print()
with open("contacts.json", "r") as f:
    people = json.load(f)["contacts"]
# loop until the user wants to quit
while True:
    print("Contact list size:", len(people))
    command = input("You can 'Add', 'Delete', 'Search', or 'Q' to quit: ").lower()

    if command == "add":
        person = add_person()
        people.append(person)
        print("Person added!")
    elif command == "delete":
        delete_contact(people)  # Pass the 'people' list to the function
    elif command == "search":
        search(people)  # Pass the 'people' list to the function
    elif command == "q":
        break  # This break is intended to exit the 'while True' loop
    else:
        print("Invalid command")
    print(people)
with open("contacts.json", "w") as f:
        json.dump({"contacts": people}, f)