def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Not enough arguments for command."
        except Exception:
            return "Error"
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def update_contact(args, contacts): 
    phone, name = args
    contacts[phone] = name
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    return contacts[args[0]]

@input_error
def show_all(contacts):
    return contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["goodbye", "close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(update_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all" and len(command) == 3:
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()