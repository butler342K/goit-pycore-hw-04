def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Invalid input. Format: add <name> <phone_number>."

def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Contact updated."
        else:
            return "Contact not found."
    except ValueError:
        return "Invalid input. Format: change <name> <new_phone_number>."

def show_phone(args, contacts):
    try:
        name = args[0]
        if name in contacts:
            return f"{name}'s phone number is {contacts[name]}."
        else:
            return "Contact not found."
    except IndexError:
        return "Invalid input. Format: phone <name>."

def show_all(contacts):
    list = "All contacts:\n"
    if contacts:
        for name, phone in contacts.items():
            list +=(f"  {name}: {phone}\n")
        return list
    else:
        return "No contacts available."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
